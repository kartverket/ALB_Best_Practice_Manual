# QC ALB QGIS Process Documentation
This workflow will generate a set of rasters needed to carry out a minimum quality control of an ALB point cloud. 

The workflow is based on QGIS >= 3.36
ALB delivery according to current version "Produktspesifikasjon Punktsky"

Remember: No use of æøå in folderpath!!

Abbrevations: 
    QPT = QGIS Processing Toolbox (Right hand side panel)
    QGM = QGIS Menu Bar (top menu)


## Fetch the Delivery

- Copy delivery folders to a fast internal disk (LiDAR loves NVMe M.2 SSDs)
- Make sure that LAZ files are 'whitelisted' by the viruscontrol 

## Create QC Folders

- `/QC`
- `/QC/COPC`
- `/QC/GRID`

## Steps

### 1. Create COPC

For faster rendering in QGIS we'll generate a cloud optimized version of the point cloud:

  - Tool = **QPT | Point cloud data management | Create COPC**
  - Select laz files
  - Set output directory to `/QC/COPC/`
  - ...wait...

### 2. Build Virtual Point Cloud (VPC)

From the COPL LAZ files we'll generate a collector file referencing to each sub tile.

  - Tool = **QPT | Point cloud data management | Build virtual point cloud (VPC)**
  - Select las files from `/QC/COPC/`
  - Enable calculate boundary polygons
  - Enable calculate statistics
  - Enable build overview point cloud
  - Set output file `/QC/alb_copc_pointcloud.vpc`
  - Enable open output file after running algorithm
  - ...wait...

### 3. Build Topobaty DTM

We'll generate a basic terrain model consisting of 'ground' and 'seabed'. In order to show any voids in the dataset we'll not use a TIN.

  - Tool = **QPT | Point cloud conversion > Export to raster**
  - Select `/QC/alb_copc_pointcloud.vpc` as input
  - Select Z as Attribute
  - Set Resolution to 1m
  - Advanced Parameters | Filter expression: `Classification = 2 OR Classification = 40`
  - Set grid output to `/QC/topobathy_1m_dtm.tif`

### 4. Build Watersurface

We'll generate a surface model consisting of ground and water surface. We'll interpolate this surface to ensure that all bathy point has a corresponding surface elevation.

  - Tool = **QPT | Point cloud conversion > Export to raster (using triangulation)**
  - Select `/QC/alb_copc_pointcloud.vpc` as input
  - Select Z as Attribute
  - Set Resolution to 1
  - Advanced Parameters | Filter expression: `Classification = 2 OR Classification = 41`
  - Set Exported to `/QC/topobathy_1m_watersurface.tif`

### 5. Calculate Water Depth

From the surface model and the topobathy model we'll generate a depth grid showing

- Tool = **QGM | Raster > Raster Calculator**
- Raster Calculation Expression: `"topobathy_1m_watersurface@1" - "topobathy_1m_dtm@1"`
- Save Result Layer to `/QC/waterdepth_1m.tif`

### 6. Generate Depth Contours

From the depth grid we'll extract 1m depth conturs. Positive values down. 

- Tool = **QGM | Raster > Extraction > Contours**
- Input: `/QC/waterdepth_1m.tif`
- Interval: 1m
- Attribute name: Depth
- Enable Produce 3D vector
- Save file to `/QC/waterdepth_1m.shp`

### 7. Calculate Density

In order to evaluate the density requirement we'll generate a 2x2m density plot for the topobathygrid. 

- Tool = **QPT | Point cloud extraction > Density**
- Set resolution = 2
- Set Filter expression = `Classification = 2 OR Classification = 40`
- Set Density to `/QC/topobathy_2m_density.tif`

### 8. Calculate Density Binary Plot at ~2m Depth

From the 2m density plot we'll generate a binary plot with 1 indicating density above 5p/m2 in the depth range from 1.5 to 2.5m below the surface.

- Tool = **QGM | Raster > Raster Calculator**
- Raster Calculation Expression: `if (("topobathy_2m_density@1" >= 20) AND (("waterdepth_1m@1"  >=  0.5) AND ("waterdepth_1m@1"  <=  2.5)),1,0)`
- Save Result Layer to `/QC/topobathy_2m_density_OK_at_2mDepth.tif`

### 9. Calculate Hex Layer (Optional)

In order to make up a AOI showing valid data we'll generate up a hexbingrid with 2m sides. 
The below approach uses the pdal density function that will be depreciated in versions after v2.6.0.

```python
import glob
import subprocess
from tqdm import tqdm

lasifiles = glob.glob('*.laz')
for lasif in tqdm(lasifiles, desc="Processing files"):
    call = 'pdal density '+lasif+' -o '+lasif+'.sqlite -f SQLite --filters.hexbin.edge_size=2'
    subprocess.run(call, shell=True)
```

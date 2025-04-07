# Airborne LiDAR Bathymetry - Best Practice Manual
<div style="text-align: right"> Ver 2025.01 </div>

## Introduction
This manual provides comprehensive guidelines on the use of Airborne LiDAR Bathymetry (ALB) in Norway. The intended audience is organizations procuring ALB and its content is based on the report "Validation and application of Airborne LiDAR Bathymetry (ALB) technology for improved management and monitoring of Norwegian rivers and lakes : a pilot study 2021-2022" carried out by Norwegian Water Resources and Energy Directorate (NVE), The Norwegian Mapping Authority (Kartverket), The Norwegian Environment Agency (Miljødirektoratet), The Norwegian Public Roads Administration (Statens vegvesen), and Hafslund Eco Vannkraft.

## Table of Contents
- [Airborne LiDAR Bathymetry - Best Practice Manual](#airborne-lidar-bathymetry---best-practice-manual)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [How to Contribute](#how-to-contribute)
  - [Licence](#licence)
- [Measurement Concept and Sensors](#measurement-concept-and-sensors)
- [ALB Pros and Cons](#alb-pros-and-cons)
- [ALB Use Cases in Norway](#alb-use-cases-in-norway)
- [ALB Procurement Process](#alb-procurement-process)
- [ALB Project Workflow](#alb-project-workflow)
- [Example Specifications](#example-specifications)
- [Quality Control](#quality-control)
- [Glossary](#glossary)
- [References](#references)
    - [Standards](#standards)
    - [Articles / Journal Papers](#articles--journal-papers)
    - [Books](#books)
    - [Reports / Technical Documentation](#reports--technical-documentation)
    - [Websites](#websites)
- [Appendix](#appendix)

## How to Contribute
The intention is that the manual has a broad ownership and changes can be proposed via pull requests or by submitting issues that we will follow up.

## Licence
This manual is licensed under the Norwegian Licence for Open Government Data (NLOD) 2.0.

# Measurement Concept and Sensors
Light Detection and Ranging (LiDAR) technology has become the primary source for capturing river geometry, enabling rapid and accurate 3D point cloud collection in shallow water where other measurement techniques, such as multibeam echosounders, are impractical or impossible to use. 

A LiDAR sensor measures the distance to a target by measuring the time between the emission of a laser pulse from a sensor and the detection of the reflected laser from the target. Depending on the wavelength, there are two types of LiDAR sensors: topographic LiDAR (ALS) and bathymetric LiDAR (ALB). Topographic LiDAR is associated with a 1064 nm laser, which cannot penetrate water and is therefore mainly used for topographic and sea surface sensing. Bathymetric LiDAR, on the other hand, uses a 532 nm laser that penetrates the water and provides bottom detection.

The ALB is the most widely used type of LiDAR for river studies that require a high degree of mapping accuracy, such as environmental river studies, sediment transport studies, and flood modeling. Currently, a variety of bathymetric LiDAR sensors are commercially available, defined by their technical specifications such as laser energy per pulse, laser footprint, and maximum detectable depth. 

The ALB verification project collected datasets from the following sensors available on the European market in 2021: Riegl VQ880-G, Riegl VQ840-G, Leica Chiroptera 4X and the Teledyne Optech CZMIL SuperNova. All three sensor manufacturers have since released updated systems, and the drone based YellowScan bathymetric LiDAR system has also gained market traction. 

Sensor types range from heavy, high-energy systems that require fixed-wing aircraft to smaller, lighter, low-energy sensors that can be mounted on a drone. The choice of sensor for bathymetric mapping depends primarily on the size of the project, whether the surrounding topography allows safe operation with fixed-wing aircraft, and sensor availability. 

The Teledyne Optech CZMIL (Coastal Zone Mapping and Imaging LiDAR) and the Leica Chiroptera 4X are airborne multi-frequency sensors used for mapping topographic surfaces and coastal zones, and their high laser energy per pulse characteristics make them particularly suitable for mapping deep depths such as those found in coastal applications. However, the higher laser penetration capabilities of CZMIL and Chiroptera come at the expense of point density, as laser energy and point density are negatively correlated.

The Riegl VQ880-G, on the other hand, is an airborne topo-bathy sensor with lower laser energy per pulse and a smaller footprint compared to the high energy systems, which can map with much higher point density but less water penetration. The Riegl VQ840-G is another topo-bathy sensor that is much lighter than traditional bathymetric LiDAR sensors and can therefore be operated from an unmanned aerial vehicle or helicopter. 

Although they share many of the same sensor components and virtually the same measurement principles, an ALB system differs significantly from a classic ALS setup. Due to the air-water-air propagation, a measurement with an ALB sensor is a function of significant limiting factors and will be more difficult to process than the ALS measurement where the light propagates only in the air. This is illustrated in the following figure by Mandlburger (2022) in his article summarizing the available active and passive methods used in bathymetric surveys. 

![Alt text for the image](/figures/Pfeifer-mandlburger-glira_2015_ALB-Concept.png)

*Fig. 1: Conceptual drawing of the principle of airborne laser bathymetry. (Mandlburger 2020)*

For the system to reliably register a seafloor return, the emitted light energy must survive a number of limiting factors. First, the energy must propagate from air to water and not be reflected at the air-water interface. Next, the light is attenuated in the water column by absorption and scattering. Finally, the seafloor must reflect a minimum amount of energy for the light to travel back up the propagation path to the ALB sensor. To calculate air-to-water and water-to-air refraction, the system must also acquire or estimate the water surface. Without modeling the water surface, the system will not be able to compute bathymetric measurements. 

Because all of these factors potentially limiting sensor performance vary from site to site and over time within a site, it can be difficult to predict the end result when ordering an ALB survey.

# ALB Pros and Cons
An overview of the advantages and disadvantages of using Airborne LiDAR Bathymetry compared to traditional surveying methods.

# ALB Use Cases in Norway
Descriptions and examples of practical applications and projects utilizing ALB technology within Norway.

# ALB Procurement Process
Guidelines and recommendations on procuring ALB services, including tendering, specifications, and evaluation criteria.

# ALB Project Workflow
Step-by-step guide through the lifecycle of an ALB project, from planning and execution to data analysis and dissemination.

# Example Specifications
Sample technical specifications and quality requirements for ALB projects.

# Quality Control 
A quality control check of the delivered dataset should be performed as soon as possible to identify deficiencies in the raw dataset as well as errors in the delivery format, report, and metadata. A minimum QC regime based on QGIS and PDAL can be found [here](/qc/ALB_QC_Steps.md).

# Glossary
**ALB (Airborne LiDAR Bathymetry)**  
A remote sensing technology using aircraft-mounted LiDAR sensors to measure seafloor and underwater terrain in shallow coastal and inland waters.

**LiDAR (Light Detection and Ranging)**  
A remote sensing method that uses light in the form of a pulsed laser to measure variable distances to the Earth.

**LAS/LAZ (LAS/LAZ file format)**  
File format designed for the interchange and archiving of lidar point cloud data. LAZ is a lossless compressed version. 

# References
Curated list of references, standards, and additional reading materials relevant to ALB practices.

### Standards
- **Produktspesifikasjon Punktsky** (current version). Kartverket. [https://sosi.geonorge.no/produktspesifikasjoner/Punktsky/] 

### Articles / Journal Papers
- **Author(s)** (Year). *Title of the article*. _Journal Name_, Volume(Issue), pages. [DOI or URL]
- **Mandlburger, G.** (2020). *A review of airborne laser bathymetry for mapping of inland and coastal waters.* _Hydrographische Nachrichten_, 116, 6–15. https://doi.org/10.23784/HN116-01

### Books
- **Author(s)** (Year). *Title of Book* (Edition, if any). Publisher. ISBN (optional).

### Reports / Technical Documentation
- **Organization or Author(s)** (Year). *Title of Report* (Report No., if available). Publisher/Organization. [URL if available]
- **NVE,Kartverket,Statens Vegvesen, Miljødirektoratet, Hafslund Eco** (2023). *Validation and application of Airborne LiDAR Bathymetry (ALB) technology for improved management and monitoring of Norwegian rivers and lakes : a pilot study 2021-2022* (NVE Rapport nr. 2/2023). NVE. [https://publikasjoner.nve.no/rapport/2023/rapport2023_02.pdf]
- **NORCE** (2022). *Application of airborne LiDAR bathymetry in Norway* (LFI-rapport nr: 46) NORCE [https://norceresearch.brage.unit.no/norceresearch-xmlui/handle/11250/3053017]


### Websites
- **Author/Organization** (Year). *Title of Webpage or Article*. Website Name. Retrieved [Date accessed], from [URL]

  **Example:**
  - **Kartverket** (2024). *Bathymetric LiDAR in Norway*. Kartverket.no. Retrieved April 5, 2024, from [https://www.kartverket.no/bathymetric-lidar-norway]

# Appendix
Supporting documents, templates, and supplementary information useful for ALB project execution and management.


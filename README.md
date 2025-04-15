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
- [Strengths and Limitations of ALB](#strengths-and-limitations-of-alb)
    - [Strengths](#strengths)
    - [Limitations](#limitations)
- [ALB Use Cases in Norway](#alb-use-cases-in-norway)
  - [River surveys](#river-surveys)
  - [Lake and reservoir surveys](#lake-and-reservoir-surveys)
  - [Marine surveys](#marine-surveys)
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
  - [List of ALB Datasets](#list-of-alb-datasets)

## How to Contribute
The intention is that the manual has a broad ownership and changes can be proposed via pull requests or by submitting issues that we will follow up.

## Licence
This manual is licensed under the Norwegian Licence for Open Government Data (NLOD) 2.0.

# Measurement Concept and Sensors

Light Detection and Ranging (LiDAR) technology has become the primary source for capturing river geometry, enabling rapid and accurate 3D point cloud collection in shallow water where other measurement techniques, such as multibeam echosounders, are impractical or impossible to use. 

A LiDAR sensor measures the distance to a target by measuring the time between the emission of a laser pulse from a sensor and the detection of the reflected laser from the target. Depending on the wavelength, there are two types of LiDAR sensors: topographic LiDAR (ALS) and bathymetric LiDAR (ALB). Topographic LiDAR is associated with a 1064 nm laser, which cannot penetrate water and is therefore mainly used for topographic and sea surface sensing. Bathymetric LiDAR, on the other hand, uses a 532 nm laser that penetrates the water and provides bottom detection.

The ALB is the most widely used type of LiDAR for river studies that require a high degree of mapping accuracy, such as environmental river studies, sediment transport studies, and flood modeling. Currently, a variety of bathymetric LiDAR sensors are commercially available, defined by their technical specifications such as laser energy per pulse, laser footprint, and maximum detectable depth. 

Sensor types range from heavy, high-energy systems that require fixed-wing aircraft to smaller, lighter, low-energy sensors that can be mounted on a drone. The choice of sensor for bathymetric mapping depends primarily on the size of the project, whether the surrounding topography allows safe operation with fixed-wing aircraft, and sensor availability. 

[Gottfried Mandlburger](https://orcid.org/0000-0002-2332-293X), a scholar at TU Wien, has over the years been following the advances of ALB sensors and has nominated the following categories as a rudimentary classification:

| Deep Bathymetric Sensors | Shallow Bathymetric Sensors |
|------------------------|----------------------------|
| • ~3× Secchi depth (i.e. 50 m @ k=0.1) | • ~1.5× Secchi depth (i.e. 25 m @ k=0.1) |
| • High pulse energy (5–7 mJ) | • Low to medium pulse energy (0.02–0.1 mJ) |
| • Low pulse repetition rate (3–10 kHz) | • High pulse repetition rate (35–550 kHz) |
| • Long pulses (2–6.5 ns = 60–200 cm) | • Short pulses (1.2–2 ns = 36–60 cm) |
| • Large laser footprints (3.5 m @ 500 m AGL) | • Small laser footprints (50 cm @ 500 m AGL) |
| • Low spatial resolution | • High spatial resolution |
| • Focus: maximum penetration | • Focus: high definition in littoral zone, rivers, etc. |
| • Application: charting coastal waters, object detection | • Application: flood simulation, habitat modelling, hydro-morphodynamics, etc. |

The Teledyne Optech CZMIL, the Fugro RAMMS and the Leica Chiroptera series of airborne multi-frequency sensors used for mapping topographic surfaces and coastal areas, and their high laser energy per pulse characteristics make them particularly well suited for mapping deep depths such as those found in coastal applications. However, the higher laser penetration capabilities of the 3xSecci sensors come at the expense of point density, as laser energy and footprint are negatively correlated.

The Riegl VQ880, on the other hand, is an airborne topo-bathy sensor with lower laser energy per pulse and a smaller footprint compared to the high energy systems, which can map with much higher point density but less water penetration. The Riegl VQ840/VQ860 is another topo-bathy sensor that is much lighter than the traditional bathymetric LiDAR sensors and can therefore be operated from an unmanned aerial vehicle or helicopter. There are also dedicated drone-based systems available, such as the Yellowscan bathymetric LiDAR system. 

Please note that this deep vs. shallow division does not apply to all sensors, as some can be configured to operate in both or hybrid mode. Therefore, it is important to be clear in the procurement documents what the end use of the dataset will be in order for the contractor to select the appropriate sensor and/or set the appropriate acquisition parameters. 

Although they share many of the same sensor components and virtually the same measurement principles, an ALB system differs significantly from a classic ALS setup. Due to the air-water-air propagation, a measurement with an ALB sensor is a function of significant limiting factors and will be more difficult to process than the ALS measurement where the light propagates only in the air. This is illustrated in the following figure by Mandlburger (2022) in his article summarizing the available active and passive methods used in bathymetric surveys. 

![Alt text for the image](/figures/Pfeifer-mandlburger-glira_2015_ALB-Concept.png)

*Fig. 1: Conceptual drawing of the principle of airborne laser bathymetry. (Mandlburger 2020)*

In order for the system to reliably detect a seafloor return, the emitted light energy must survive a number of limiting factors. First, the energy must propagate from air to water and not be reflected at the air-water interface. Next, the light is attenuated in the water column by absorption and scattering. Finally, the seafloor must reflect a minimum amount of energy for the light to travel back up the propagation path to the ALB sensor. To calculate air-to-water and water-to-air refraction, the system must also acquire or estimate the water surface. Without modeling the water surface, the system will not be able to compute bathymetric measurements. As a side note, sunlight can affect the noise level in the sensor receiver, and a greater depth range can be achieved by flying at night.  

Because all of these factors potentially limiting sensor performance vary from site to site and over time within a site, it can be difficult to predict the end result when ordering an ALB survey.

# Strengths and Limitations of ALB
An overview of the advantages and disadvantages of using airborne LiDAR bathymetry versus traditional surveying methods.

### Strengths
- The only acquisition approach that produces a homogeneous terrain model consisting of both bathymetry and topography.
- Very efficient acquisition rate in shallow water. With a ~3 secci sensor operating at an altitude of 450m, we have experienced an concistent acquisition rate of 13 km2/h including line turns. Establishing bathymetry with ALB in shallow water will make complementary multibeam acquisition from surface vessels more efficient. 
- Not prone to challenging sound profiles where fresh and salt water mix in estuaries and river inlets. These are areas where we experience large spatial and temporal variations that introduce significant errors when mapping with sonar.
- A pure remote sensing acquisition method without the need for people or boats in remote, potentially dangerous or ecologically sensitive areas.

### Limitations
- Sensor performance, generally the depth range achieved, depends on several physical and environmental factors that are difficult to assess and predict. First, the seafloor must have a reflectivity above a certain threshold and one must have a line-of-sight to the sensor free of obstructions and vegetation (physical factors). Second, weather, sea state, amount of suspended sediment and rock/glacial debris in the water column will degrade performance.
- A successful mapping campaign requires good acquisition timing. When mapping in marine environments, large algal blooms must be avoided, and when mapping rivers and lakes, water quality, turbulence, whitewater and rapids, and biomass in the water will either absorb or scatter laser energy. Timing the perfect acquisition window with commercially available sensors can be challenging.
- Classifying a bathymetric point cloud is challenging, especially in low-density datasets where a geometric or statistical approach begins to fail and one must resort to more manual interpretation. 
- Mapping the exact transition zone between "wet" and "dry" is challenging, and it can be difficult to distinguish the sea surface from the seafloor. This is due to both sensor design and how the system distinguishes between points in the water and points on the dry, but environmental factors such as waves and submerged vegetation can make resolving the correct point a challenge.


# ALB Use Cases in Norway

Norwegian government agencies have been evaluating the potential of the ALB sensor for nearly 30 years. The Norwegian Hydrographic Service (NHS), together with Tenix LADS Corporation, conducted extensive tests in 1998 and 2002. NHS also investigated the performance of the then-new Riegl VQ-820 sensor in 2014 and the Optech Titan in 2017.

The evolution of ALB sensor technologies has been high and in 2019 the current generation of Riegl, Hexagon and Optech sensors were evaluated by an ALB working group over a range of river types. However, the delivery was not a direct comparative study of sensors, but rather an in-depth investigation into the use of ALB as a tool for more efficient management of rivers and freshwater bodies. 

## River surveys 
Since 2019, NVE, Skagerak Energi and Hafslund Eco have mapped more than 30 rivers and ALB is the de facto dataset that provides input for accurate hydraulic models and hydro-morphological analyses, such as monitoring sediment transport and erosion over time and simulating flood mitigation programs.
- 2021 Bøelva
- 2021 Lærdalselva
- 2021 Lærdalselva Drone
- 2021 Glomma
- 2021 Tangelva, Gjermåa and Leira
- 2021 Hallingdalselven


## Lake and reservoir surveys
To create a seamless elevation model and provide a dataset suitable for habitat and ecosystem management, ALB has been used to complement multibeam measurements. ALB has also been used to accurately map hydroelectric reservoirs to monitor sedimentation and facilitate volume estimation.
- 2018 Benna
- 2020 Benna
- 2021 Selbusjøen
- 2021 Krøderen
  
## Marine surveys 
A number of ALB surveys have been conducted in the marine environment with the intention of providing a set of test areas from different parts of Norway where one can investigate ALB as a source for coastal habitat mapping. ALB is also an important tool for producing hazard maps for fast clay landslides near the coastal zone. 
- 2021 Helligvær
- 2021 Bliksvær
- 2021 Fjøløy
- 2023 Fauske
- 2024 Færder Nasjonalpark

# ALB Procurement Process

Guidelines and recommendations on procuring ALB services, including tendering, specifications, and evaluation criteria.

*_WORK IN PROGRESS_*

# ALB Project Workflow

Step-by-step guide through the lifecycle of an ALB project, from planning and execution to data analysis and dissemination.

*_WORK IN PROGRESS_*

# Example Specifications

*_HER ØNSKER JEG AT VI LEGGER INN MALER FOR TEKNISK SPESIFIKASJON. ENKLESTE ER Å LENKE INN WORD DOKUMENTER MED ÅRSREVISJONER_* 

Sample technical specifications and quality requirements for ALB projects.

# Quality Control 
A quality control check of the delivered dataset should be performed as soon as possible to identify deficiencies in the raw dataset as well as errors in the delivery format, report, and metadata. A minimum QC regime based on QGIS and PDAL can be found [here](/qc/ALB_QC_Steps.md).

# Glossary
**ALB (Airborne LiDAR Bathymetry)**  
A remote sensing technology using aircraft-mounted LiDAR sensors to measure seafloor and underwater terrain in shallow coastal and inland waters.

**k value**
Define k value here

**LiDAR (Light Detection and Ranging)**  
A remote sensing method that uses light in the form of a pulsed laser to measure variable distances to the Earth.

**LAS/LAZ (LAS/LAZ file format)**  
File format designed for the interchange and archiving of lidar point cloud data. LAZ is a lossless compressed version.

**SECCI**
Define SECCI here

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
## List of ALB Datasets

| Dataset                                                                                          | Acquisition Year   | Contractor                     | Dataset Owner     |
|:-------------------------------------------------------------------------------------------------|:-------------------|:-------------------------------|:------------------|
| [Batymetri Fjøløy 2013](https://hoydedata.no/laserinnsyn2?id=5327)                               | 2013               | Statens Kartverk Sjødivisjonen | Kartverket        |
| [Hafslund Elvekartlegging Geilo 2015](https://hoydedata.no/laserinnsyn2?id=6122)                 | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Gol 2015](https://hoydedata.no/laserinnsyn2?id=6123)                   | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Hallingdalselve Hol 2015](https://hoydedata.no/laserinnsyn2?id=6126)   | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Hallingdalselve Torpo 2015](https://hoydedata.no/laserinnsyn2?id=6127) | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Hovet 2015](https://hoydedata.no/laserinnsyn2?id=6129)                 | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Nes 2015](https://hoydedata.no/laserinnsyn2?id=6128)                   | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [Hafslund Elvekartlegging Ål 2015](https://hoydedata.no/laserinnsyn2?id=6124)                    | 2015               | Statens Kartverk               | Hafslund-Eco      |
| [NVE Driva 2016](https://hoydedata.no/laserinnsyn2?id=871)                                       | 2016               | Terratec AS                    | NVE               |
| [NVE Gaula 2016](https://hoydedata.no/laserinnsyn2?id=881)                                       | 2016               | Terratec AS                    | NVE               |
| [NVE Gudbrandsdalslågen 2016](https://hoydedata.no/laserinnsyn2?id=1031)                         | 2016               | Terratec AS                    | NVE               |
| [NVE Mandalselva 2016](https://hoydedata.no/laserinnsyn2?id=829)                                 | 2016               | Terratec AS                    | NVE               |
| [NVE Skiens og Porsgrunnselva 2016](https://hoydedata.no/laserinnsyn2?id=828)                    | 2016               | Terratec AS                    | NVE               |
| [NVE Storelva Randselva Begna 2016](https://hoydedata.no/laserinnsyn2?id=873)                    | 2016               | Terratec AS                    | NVE               |
| [Batymetri Søre Sunnmøre 2017](https://hoydedata.no/laserinnsyn2?id=910)                         | 2017               | Statens Kartverk               | Kartverket        |
| [Hornindalsvatnet dybde 2017](https://hoydedata.no/laserinnsyn2?id=1137)                         | 2017               | Statens Kartverk               | Miljødirektoratet |
| [NDH Søre Sunnmøre dybdedata 2017](https://hoydedata.no/laserinnsyn2?id=876)                     | 2017               | Terratec AS                    | Kartverket        |
| [NVE Eidselva 5pkt 2017](https://hoydedata.no/laserinnsyn2?id=3754)                              | 2017               | Terratec AS                    | NVE               |
| [NVE Etneelva 5pkt 2017](https://hoydedata.no/laserinnsyn2?id=3753)                              | 2017               | Terratec AS                    | NVE               |
| [NVE Figgjo 5pkt 2017](https://hoydedata.no/laserinnsyn2?id=3752)                                | 2017               | Terratec AS                    | NVE               |
| [NVE Nausta 5pkt 2017](https://hoydedata.no/laserinnsyn2?id=3751)                                | 2017               | Terratec AS                    | NVE               |
| [Selbusjøen dybde 2017](https://hoydedata.no/laserinnsyn2?id=1115)                               | 2017               | Statens Kartverk               | Miljødirektoratet |
| [NVE Hååna (2017/2018/2019)](https://nve.no)                                                     | 2017/2018/2019     | TerraTec                       | NVE               |
| [NVE Kvina og Litleåna (2017/2018/2019)](https://nve.no)                                         | 2017/2018/2019     | TerraTec og AHM                | NVE               |
| [Eikesdalsvatnet dybde 2018](https://hoydedata.no/laserinnsyn2?id=1142)                          | 2018               | Statens Kartverk               | Miljødirektoratet |
| [NVE - Litleåna-Kvina 4pkt 2018](https://hoydedata.no/laserinnsyn2?id=5432)                      | 2018               | Terratec AS                    | NVE               |
| [NVE Flåmselvi 2018](https://hoydedata.no/laserinnsyn2?id=1018)                                  | 2018               | Terratec AS                    | NVE               |
| [NVE Hååna 5pkt 2018](https://hoydedata.no/laserinnsyn2?id=5049)                                 | 2018               | Terratec AS                    | NVE               |
| [NVE Jølstra-Anga 5pkt 2018](https://hoydedata.no/laserinnsyn2?id=5050)                          | 2018               | Terratec AS                    | NVE               |
| [NVE Lærdal 2018](https://hoydedata.no/laserinnsyn2?id=1091)                                     | 2018               | Statens Kartverk               | NVE               |
| [NVE Lærdalselva 5pkt 2018](https://hoydedata.no/laserinnsyn2?id=5060)                           | 2018               | Terratec AS                    | NVE               |
| [NVE Nidelva 2018](https://hoydedata.no/laserinnsyn2?id=1019)                                    | 2018               | Terratec AS                    | NVE               |
| [NVE Numedalslågen 2018](https://hoydedata.no/laserinnsyn2?id=1029)                              | 2018               | Terratec AS                    | NVE               |
| [NVE Opo 2018](https://hoydedata.no/laserinnsyn2?id=1020)                                        | 2018               | Terratec AS                    | NVE               |
| [NVE Rauma 2018](https://hoydedata.no/laserinnsyn2?id=1016)                                      | 2018               | Terratec AS                    | NVE               |
| [NVE Tovdalselva 2018](https://hoydedata.no/laserinnsyn2?id=1015)                                | 2018               | Terratec AS                    | NVE               |
| [NVE Vosso 5pkt 2018](https://hoydedata.no/laserinnsyn2?id=5031)                                 | 2018               | Terratec AS                    | NVE               |
| [Salvatnet dybde 2018](https://hoydedata.no/laserinnsyn2?id=1139)                                | 2018               | Statens Kartverk               | Miljødirektoratet |
| [Hovsvatn dybde 13pkt 2019](https://hoydedata.no/laserinnsyn2?id=1173)                           | 2019               | Terratec AS                    | Nye Veier         |
| [NVE dronetest Figgjo (2020)](https://nve.no)                                                    | 2020               | Nordic Unmanned                | NVE               |
| [SVV RV7 Lindelien - Kittilsviki (2020)](https://vegvesen.no)                                    | 2020               | Nearshore Survey / Terratec    | SVV               |
| [Dybdedata Randselva-Storelva 2020](https://hoydedata.no/laserinnsyn2?id=4224)                   | 2020               | Statens Kartverk               | Ringerike kommune |
| [Fjøløy vår -MGK ALB Pilot 2021](https://hoydedata.no/laserinnsyn2?id=5597)                      | 2021               | Terratec AS                    | Kartverket        |
| [NDH Bøelva Chiroptera 2021](https://hoydedata.no/laserinnsyn2?id=5799)                          | 2021               | Hexagon                        | NDH               |
| [NDH Bøelva Riegl 840 (2021)](https://kartverket.no)                                             | 2021               | Terratec                       | NDH               |
| [NDH Bøelva Riegl 880 (2021)](https://kartverket.no)                                             | 2021               | AHM                            | NDH               |
| [NDH Glomma CZMIL 2021](https://hoydedata.no/laserinnsyn2?id=5794)                               | 2021               | Terratec AS                    | NDH               |
| [NDH Glomma Chiroptera 2021](https://hoydedata.no/laserinnsyn2?id=5798)                          | 2021               | Hexagon                        | NDH               |
| [NDH Glomma MBES 2021](https://hoydedata.no/laserinnsyn2?id=5803)                                | 2021               | Statens Kartverk               | NDH               |
| [NDH Krøderen CZMIL 2021](https://hoydedata.no/laserinnsyn2?id=5796)                             | 2021               | Terratec AS                    | NDH               |
| [NDH Krøderen Riegl 840 (2021)](https://kartverket.no)                                           | 2021               | Terratec                       | NDH               |
| [NDH Krøderen Riegl 880 (2021)](https://kartverket.no)                                           | 2021               | AHM                            | NDH               |
| [NDH Lærdalselvi CZMIL 2021](https://hoydedata.no/laserinnsyn2?id=5795)                          | 2021               | Terratec AS                    | NDH               |
| [NDH Lærdalselvi Riegl 840 (2021)](https://kartverket.no)                                        | 2021               | TerraTec                       | NDH               |
| [NDH Lærdalselvi Riegl 880 (2021)](https://kartverket.no)                                        | 2021               | AHM                            | NDH               |
| [NDH Selbusjøen CZMIL 2021](https://hoydedata.no/laserinnsyn2?id=5797)                           | 2021               | Terratec AS                    | NDH               |
| [NDH Selbusjøen Chiroptera 2021](https://hoydedata.no/laserinnsyn2?id=5800)                      | 2021               | Hexagon                        | NDH               |
| [NDH Tangeelva Riegl 880 (2021)](https://kartverket.no)                                          | 2021               | AHM                            | NDH               |
| [NDH Tangelva Chiroptera 2021](https://hoydedata.no/laserinnsyn2?id=5801)                        | 2021               | Hexagon                        | NDH               |
| [NDH Topobaty Bliksvær 2021](https://hoydedata.no/laserinnsyn2?id=5436)                          | 2021               | Terratec AS                    | NDH               |
| [NDH Topobaty Helligvær 2021](https://hoydedata.no/laserinnsyn2?id=5435)                         | 2021               | Terratec AS                    | NDH               |
| NVE - 2023/2023/2024                                                                             |                    |                                | NVE               | 
| Hafslund Eco - 2023/2023/2024                                                                    |                    |                                | Hafslund-Eco      |
| Skagerak Energi - 2023/2023/2024                                                                 |                    |                                | Skagerak Energi   | 
| [Beiarelva Batymetri 2023](https://hoydedata.no/laserinnsyn2?id=6142)                            | 2023               | Field                          | Geovekst          |
| [Fauske Batymetri 2023](https://hoydedata.no/laserinnsyn2?id=6142)                               | 2023               | Field                          | Geovekst          |
| [Færder topobathy 2024](https://hoydedata.no/laserinnsyn2?id=6142)                               | 2024               | Hexagon                        | Geovekst          |
# APPENDIX C: Procurement of MBES – Technical Specification

For waterbodies where ALB does not give complete coverage one can consider complementing the ALB with a Multibeam Echo Sounder (MBES) survey. To minimize time in field, one should acquire MBES after actual coverage of the ALB survey has been delivered.

Based on the Norwegian Hydrographic Service specification – [Teknisk kravspesifikasjon for sjømåling (Norwegian only)](https://www.kartverket.no/til-sjos/sjokart/godkjenningsordning-for-sjokartlegging), a minimum specification for MBES acquisition for river and lake mapping is proposed:

---

## Minimum MBES Acquisition Technical Specifications

The MBES deliverable must meet the general requirements for MBES point clouds as stated in [Produktspesifikasjon Punktsky](https://sosi.geonorge.no/produktspesifikasjoner/Punktsky/), and the deliverable must meet the accuracy requirements and the point density for a category [Psky_1_MBES_B](https://sosi.geonorge.no/produktspesifikasjoner/Punktsky/#truemultistr%C3%A5le-ekkolodd) survey.

### Table: Requirement for the acquisition, processing, and reporting must be carried out to the following demands:

| Demand Ref. in [NMA MBES](https://www.kartverket.no/til-sjos/sjokart/godkjenningsordning-for-sjokartlegging) | Requirement                       | Description |
|---------------|-----------------------------------|-------------|
| K2.2          | **Positioning**                   | The positioning must be done using an INS system capable of meeting the accuracy requirements stated for `Psky_1_MBES_A`. |
| K2.3          | **Echosounder**                   | The sonar must be capable of meeting the accuracy requirements stated for `Psky_1_MBES_A`. For survey in very shallow water a high beam angle is allowed. |
| K2.4          | **Motion Sensor**                 | The vessel motion must be derived from an INS system capable of meeting the accuracy requirement stated for `Psky_1_MBES_A`. The system must resolve heading using a dual antenna setup. |
| K2.6          | **Sound velocity profiles**       | The survey must collect sound velocity profiles in waterbodies deeper than 10 m. |
| K2.7          | **Sound velocity at Sonar Head**  | The survey system must include a SV sensor at the sonar head and the sound velocity must be interfaced to the sonar in real time. |
| K3.1          | **CRS - Horizontal**              | `EUREF89 / UTM Local Sone (EPSG: 5972 / 5973 / 5975)` |
| K3.2          | **CRS – Vertical**                | `NN2000` geoid model *(version used must be reported)* |
| K3.3          | **Time Reference**                | UTC |
| K4.1          | **Horizontal positioning accuracy (absolute)** | `0.50 m + 0.016 * depth` |
| K4.2          | **Vertical positioning accuracy (absolute)**   | `0.12 m + 0.002 * depth` |
| K4.3          | **Vertical positioning precision**             | `0.08 m + 0.002 * depth` |
| K4.4          | **Accuracy Control**              | The MBES accuracy is to be proven using the ALB dataset. The overlap between ALB and MBES must be large enough to ensure a statistically robust comparison. |
| K4.8          | **Density**                       | The survey plan must ensure the attempt of 100% coverage of the seabed. The point density for bathymetric points must be fulfilled within 80% of all 2×2 m cells within a 10×10 m grid. <br>Ref: *Produktspesifikasjon Punktsky* category A. |
| K5.1          | **Sensor and System Calibration** | Report must include documents showing valid sensor calibration certificates (SVP) and sensor installation calibration (offset surveys). |
| K5.2          | **System Verification**           | Report must include document showing valid system verification (Patch Test). |
| K8.1.d        | **Report**                        | The survey report must include:<br>- Survey Name<br>- Survey Company<br>- Client<br>- Survey description and plot of AOI<br>- CRS (horizontal, vertical, time)<br>- Total Area, survey dates<br>- Survey Platform Description<br>- Survey Sensor Description<br>- Acquisition Report<br>- Processing Report<br>- Personnel (Surveyor, Processor, Overall Project Responsible Person) |
| K8.2          | **Data Delivery**                 | ASPRS LAS in agreement with the requirements stated in *Produktspesifikasjon Punktsky* |

---

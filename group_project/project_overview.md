# **Project: Machine Learning Analysis of Temperature–Biology Coupling in Global Oceans**  
**Predicting Phytoplankton Productivity and Marine Heatwave Impacts from Satellite Remote Sensing**

---

## **Data Description (Updated)**  
This project integrates three major NASA/NOAA Earth‑observation datasets, each processed into an analysis‑ready form through a multi‑phase workflow (local feasibility → Dask → SDSC → Spark ML). All datasets are scientific-grade Level‑3 products distributed in NetCDF format and reprocessed into Parquet for scalable machine learning.

### **1. NOAA OISST v2.1 — Daily Sea Surface Temperature**  
- Daily, global SST at 0.25° (~25 km)
- 1981–present
- Used as the core climate predictor
- Provides temperature, anomalies, error estimates, and ice masks
- Source: NOAA NCEI OISST v2.1 archive

### **2. VIIRS JPSS‑1 Level‑3 Mapped Chlorophyll (chlor_a), Daily**
- **Resolution:** ~4 km, Global, Daily (Level-3 Mapped)
- **Source:** NASA OB.DAAC (e.g., `JPSS1_VIIRS.20200119.L3m.DAY.CHL.chlor_a.4km.nc`)
- **Key Decision:** We switched from 8-Day composites to **Daily** files to match the temporal resolution of the SST data.
- **Trade-off:** This introduces significant sparsity. ~90% of pixels are masked due to cloud cover. We handle this by filtering for clear-sky "matchups" during training.
- **Variable:** *chlor_a* (mg $m^{-3}$)
  

### **3. NSIDC NOAA/NSIDC CDR Sea Ice Concentration v5 (25 km Polar Stereographic)**  
- Daily gridded sea‑ice concentration
- Polar stereographic grid (EPSG:3411), ~25 km resolution
- 1978–present
- Used to mask biologically invalid, ice‑covered waters
- Variable: *cdr_seaice_conc* (0–1 after scaling)

### Combined Dataset (After Processing)
- Fully regridded to SST grid
- Temporally aligned (daily SST/ice matched to nearest CHL composite)
- Ice‑masked chlorophyll fields
- Multi‑year global coverage
- Output stored as partitioned Parquet for Spark ML

---

## **Project Outline (Updated)**

### **Problem**  
Global warming is restructuring marine ecosystems by changing sea surface temperatures, stratification, and nutrient supply. These shifts alter phytoplankton abundance and productivity.
Machine learning provides a way to uncover patterns and predict biological responses across space and time.

### **Core Datasets and Roles**  
- **SST:** Climate driver (temperature, anomalies, seasonality)
- **Chlorophyll:** Biological response (productivity, blooms)
- **Sea Ice:** Polar boundary condition (masking and ecological zone separation)

Total data volume (5–10 years): ~35–45 GB before preprocessing.

---

## **Research Questions & Methods (Updated)**
### **Data Constraints & Physical Reality**
A critical challenge in satellite oceanography is **Cloud Cover**.
* **SST (Microwave):** Available 100% of the time (sees through clouds).
* **Chlorophyll (Optical):** Blocked by clouds. In winter North Pacific, valid data retention is **~5-10%**.
* **Strategy:** We filter for high-quality, clear-sky pixels for training (Phase 3). Future phases will explore **Imputation** (using SST to predict missing chlorophyll) to recover lost data.
  
### **QUESTION 1 — What are Earth’s major ocean ecological zones?**  
**Method:** K‑Means Clustering on SST + chlorophyll + latitude
**Purpose:** Identify emergent biophysical zones
**Expected Insight:**
Distinct temperature–biology clusters such as:
- tropical oligotrophic deserts
- temperate productive waters
- polar productive zones
- upwelling systems
- subtropical gyres

**Output:** Global cluster map showing major ecological regimes.

---

### **QUESTION 2 — Can we predict phytoplankton blooms using temperature?**  
**Method:** Random Forest Classification
**Target:** Bloom presence, defined via percentile‑based chlorophyll threshold
**Features:**
SST, SST anomalies, day‑of‑year, latitude

**Expected Insight:**
Temperature anomalies promote blooms in some regions but suppress them in others.

**Output:** Spatial bloom probability maps; feature importance curves.

---

### **QUESTION 3 — How much chlorophyll can be predicted from temperature alone?**  
**Method:** Gradient‑Boosted Trees / XGBoost‑style Regression
**Features:**
SST anomaly, seasonal cycle, lat/lon, lagged SST

**Expected Outcome:**
Moderate-to-strong ability (e.g., >50% variance explained) to predict chlorophyll variability from temperature signals.

**Output:** Prediction vs observation plots, error heatmaps.

---

### **QUESTION 4 — Where is the temperature–biology coupling strongest?**  
**Method:** Spatial Correlation Analysis
Compute correlations between SST anomalies and chlorophyll values for each grid cell.

**Expected Insight:**
- Negative correlation in stratified tropics
- Positive correlation in high latitudes (temperature limitation)
- Transitional behavior in midlatitudes

**Output:** Global SST–chlorophyll correlation map.

---

## **Case Study: The 2020 Pacific Marine Heatwave**  
Using anomalies derived from OISST and chlorophyll composites:

- SST anomaly: +3°C over NE Pacific
- Observed chlorophyll decline: ~40% 
- ML model predicted decline: ~35%

**Interpretation:**
The model captures large‑scale biological responses to extreme warming events, demonstrating predictive potential for marine heatwaves.

---

## **Conclusion **  
- Sea surface temperature is a powerful predictor of phytoplankton variability.
- Machine learning can detect and model complex oceanographic patterns across scales
- Ecological zones emerge naturally from combined temperature–biology features.
- Extreme events such as heatwaves can be analyzed and partially forecasted using ML.
- Regional differences require zone‑specific or latitude‑aware models.

### **Potential Applications**  
- Fisheries management
- Climate monitoring and marine heatwave early warning
- Assessing biological impacts of long‑term warming
- Ecosystem forecasting tools
- Scientific visualization and public communication

---

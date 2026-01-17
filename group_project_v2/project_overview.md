# **Project: Machine Learning Fusion of ICESat-2 Elevation Change and GRACE Mass Change**  
**Predicting Ice‑Sheet Mass Balance and Subglacial Hydrology from Satellite Altimetry and Gravimetry**

---

## **Data Description (Updated for Ice Sheets)**  
This project integrates two major NASA datasets — GRACE/GRACE‑FO mascon gravity fields and ICESat‑2 ATL06 land‑ice elevation tracks — into a unified ML‑ready dataset processed through a scalable workflow (local feasibility → SDSC → Spark ML). All data are standard scientific NetCDF/HDF5 and reprocessed into Parquet for large‑scale analysis.

### **1. GRACE/GRACE‑FO RL06.2 Mascons (CSR) — Monthly Mass Change**  
- url: [GRACE](https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/)
- Monthly mass‑anomaly fields for 2002–2024  
- Global 0.5° mascon grid  
- Includes standard geophysical corrections  
- Used as the *target variable* for supervised ML  
- Source: CSR Mascon RL06.2 archive (NetCDF)

### **2. ICESat‑2 ATL06 — Land Ice Height (Track‑Level)**
- url: [ICESat-2](https://nsidc.org/data/atl06/versions/7)
- High‑precision surface elevation from photon‑counting lidar  
- 2018–present  
- Sub‑100 m along‑track resolution  
- Provides time‑evolving elevation change critical for diagnosing thinning/thickening  
- Large dataset (~50–100GB for Greenland multi‑year extraction)  
- Source: NSIDC (Earthdata Login required)

### Combined Dataset (After Processing)  
- ATL06 tracks aggregated to monthly or seasonal elevation‑change features  
- Spatially matched to GRACE mascon footprints  
- Outlier‑filtered for slope, photon count, and geolocation flags  
- Stored as partitioned Parquet, enabling distributed ML at SDSC

---

# **Project Outline (Rewritten for GRACE + ICESat‑2)**

## **Problem**  
Ice‑sheet mass balance is a top Earth Science Decadal priority because Greenland and Antarctica are major contributors to global sea‑level rise.  
While GRACE provides direct mass‑change observations, its spatial resolution is coarse and physically complex.  
ICESat‑2 provides fine‑scale elevation change, but converting this to mass requires physical modeling.

Machine learning offers a new pathway:  
**Can we learn predictive mappings between high‑resolution elevation change and coarse‑resolution mass change?**

---

## **Core Datasets and Roles**  
- **ATL06 (ICESat‑2):** High‑resolution surface‑elevation change (geometry driver)  
- **GRACE Mascons:** Low‑resolution mass‑change signal (gravity response)  

Total volume (multi‑year Greenland subset): ~50–85GB before analytics.

---

# **Research Questions & Methods (Adapted)**

### **Data Constraints & Physical Reality**  
A challenge in altimetry–gravimetry fusion is scale mismatch.  
- **ATL06:** Dense, high‑resolution tracks  
- **GRACE:** Coarse mascon footprints  
- **Strategy:** Aggregate ATL06 into region‑level time series and use ML to learn the nonlinear relationship between geometry and mass.

---

## **QUESTION 1 — What are the major elevation‑change regimes in Greenland?**  
**Method:** K‑Means Clustering on elevation‑change metrics (dh/dt, seasonal cycle, slope, latitude)

**Purpose:** Identify emergent dynamical zones such as:  
- rapidly thinning outlet glaciers  
- stable interior ice  
- seasonal melt‑driven surface changes  
- marine‑terminating glacier basins  

**Output:** Regime map of Greenland capturing natural ice‑dynamical classes.

---

## **QUESTION 2 — Can elevation change predict monthly mass change?**  
**Method:** Gradient‑Boosted Trees / Random Forest Regression  
**Target:** GRACE mass‑change anomaly for each mascon  
**Features:**  
- ATL06 elevation‑change rates  
- seasonal metrics  
- latitude/longitude  
- lagged elevation change (lead–lag response)  

**Expected Insight:**  
Regions with strong dynamic thinning should show predictive coupling between ICESat‑2 geometry and GRACE mass.  
Model may reveal where gravitational changes lag elevation changes.

**Output:** Baseline predictive map of mass‑change skill.

---

## **QUESTION 3 — How much of GRACE’s signal is explainable from elevation change alone?**  
**Method:** XGBoost‑style regression with feature importance ranking

**Features:**  
- dh/dt  
- interannual elevation anomaly  
- dynamic thickening/thinning patterns

**Expected Outcome:**  
Moderate reproduction of mass‑change anomaly fields, particularly in:  
- fast outlet glaciers  
- marine‑terminating basins  
- interior accumulation zones  

**Output:** Explained variance heatmap over mascons.

---

## **QUESTION 4 — Where is geometry–mass coupling strongest?**  
**Method:** Spatial correlation between ATL06 elevation time series and GRACE mascons  
**Expected Insight:**  
- Strong positive coupling at major outlet glaciers  
- Weak coupling over high interior plateau  
- Complex coupling in areas with subglacial hydrology activity  

**Output:** Greenland‑wide coupling map.

---

# **Case Study Example: 2019–2021 Greenland Melt Seasons**  
Using ATL06 seasonal elevation anomalies and GRACE mass signals:

- Rapid thinning in 2020 corresponds to large negative GRACE anomalies  
- ML model captures timing and magnitude with reasonable fidelity  

**Interpretation:**  
ML can recover large‑scale mass‑change signals using only elevation data, even without explicit physical modeling.

---

# **Conclusion**  
- ICESat‑2 provides high‑resolution diagnostics of ice‑sheet geometry changes.  
- GRACE provides mass‑change truth, but at coarse resolution.  
- ML serves as a bridge that learns fine‑to‑coarse relationships.  
- Spatially coherent dynamical regimes emerge naturally from clustering.  
- Predictive modeling has potential to augment or emulate GRACE‑like products.  

# **Potential Applications**  
- Sea‑level rise assessments  
- Ice‑sheet early‑warning indicators  
- Rapid melt detection  
- Data fusion for future cryosphere missions  
- Tools for cryosphere visualization and outreach  

---


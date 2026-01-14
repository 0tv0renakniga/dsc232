# PHASE 1: Local Feasibility Pipeline

---

## Step 1: Download Data
Goal: Download datasets

### VIIRS JPSS‑1 Level‑3 Mapped Chlorophyll (chlor_a), 8‑Day Composites
#### Chlorophyll Data (ex: JPSS1_VIIRS.20200101_20200108.L3m.8D.CHL.chlor_a.4km.nc)
https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/NOAA20-VIIRS/2020/01-Jan-2020/

### NSIDC NOAA/NSIDC CDR Sea Ice Concentration v5 (25 km Polar Stereographic)
#### Sea-Ice data (ex: sic_psn25_20200101_F17_v05r00.nc)
https://noaadata.apps.nsidc.org/NOAA/G02202_V5/north/daily/2020/

### NOAA OISST v2.1 — Daily Sea Surface Temperature
#### SST (ex: oisst-avhrr-v02r01.20200101.nc)
https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/202001/

---

## Step 2: Load with xarray
Goal: Verify that files are readable and metadata is intact.

How to proceed:

Open a Python session (local machine or UCSD Datahub).
Load SST, chlorophyll, and sea‑ice files individually using xarray’s open_dataset.
Print dataset summaries using .info() and .variables.
Verify key variables exist:
SST: sst or analysed_sst
Chlorophyll: chlor_a
Sea‑ice: cdr_seaice_conc

---

## Step 3: Subset Small Region
Goal: Reduce data size so testing is fast.

How to proceed:

Choose a region (e.g., North Pacific: lat 20–40°, lon −160 to −140).
Use xarray indexing or .sel() to slice each dataset to the same region.
For sea ice (which is on a projected grid), postpone spatial subsetting until after regridding.

---

## Step 4: Do Approximate Regridding
Goal: Force all three datasets onto the same grid so they can be merged.

How to proceed:

Choose one dataset as the “reference grid” — SST is the easiest.
Regrid chlorophyll to SST grid using .interp_like().
Regrid sea‑ice concentration to SST grid (this is more approximate, but fine for feasibility).
Ignore projection complexities for now; you only need the feasibility demonstration.

---

## Step 5 — Do Approximate Time Matching
Goal: Align SST (daily), CHL (8‑day), and sea‑ice (daily) to the same time.

How to proceed:

Extract the SST file’s timestamp.
Choose the CHL file whose composite window contains or is closest to that date.
For sea ice, use the corresponding daily file.
For the feasibility step, nearest‑neighbor matching is acceptable.

---

## Step 6 — Flatten to DataFrame
Goal: Convert the aligned xarray dataset into a tidy, Spark‑ready format.

How to proceed:

After regridding and time matching, combine variables into a single xarray dataset.
Convert to a pandas DataFrame using .to_dataframe().reset_index().
Keep only columns you need:
lat, lon, time, sst, chlor_a, sea_ice_conc
Save this to a local Parquet file:
sample.parquet

---

## Step 7: Make Basic Plots
Goal: Generate visuals needed for Milestone 2 and to show your team the project is viable.

How to proceed:

Map of chlorophyll (lat vs lon)
Scatterplot of SST vs chlorophyll
Histogram of SST and chlorophyll
Map of sea‑ice concentration (as a sanity check)

---

## Step 8: Update README for Milestone 2
Goal: Document everything for your submission.

How to proceed:

Describe where the data came from.
State that this is a Phase 1 feasibility test.
Include explanations of:
dataset structure
region subset
regridding method
time alignment
basic statistics and plots
Upload all notebooks/scripts to GitHub.

---

## Summary of Phase 1
We now have:

Downloaded 1–3 sample files
Loaded them with xarray
Subset to a small region
Regridded everything to SST grid
Time‑matched all datasets
Flattened into a dataframe
Generated exploratory plots
Documented the feasibility test



# **PHASE 3 — SDSC FULL PIPELINE (Step‑by‑Step Guide)**  
This stage transforms your working Dask prototype into a **production‑scale preprocessing pipeline** that operates across years of SST, chlorophyll, and sea‑ice files on SDSC hardware.

UC San Diego researchers routinely use SDSC’s HPC systems for large‑scale scientific workflows, including Python‑based data processing, climate analyses, and high‑performance analytics 

Your pipeline now joins that tradition.

────────────────────────────────────────
## **Step 1 — Request or Confirm SDSC Access**
SDSC provides researchers access to national supercomputing resources at no cost via ACCESS allocations and supports large‑scale CPU/GPU jobs

How to proceed:
- Confirm that your ACCESS account is active.
- Request project storage if needed (SDSC offers cloud and project storage 
- Log in to SDSC through SSH or a web portal (depending on system).

Your goal: establish an environment where long‑running preprocessing jobs can run uninterrupted.

────────────────────────────────────────
## **Step 2 — Transfer Data to SDSC using Globus or High‑Speed Tools**
UC San Diego provides high‑speed transfer tools like **Globus** and the campus research network to move large datasets between systems

How to proceed:
- Use Globus endpoint on SDSC and your local machine.
- Transfer:
  - raw chlorophyll files  
  - raw SST files  
  - raw sea‑ice files  
- Organize them under structured directories:
  - `/project/raw/sst/`
  - `/project/raw/chl/`
  - `/project/raw/ice/`

────────────────────────────────────────
## **Step 3 — Set Up a Dask/Parallel Environment on SDSC**
SDSC systems support large‑scale Python workflows, including distributed memory jobs needed for scientific data processing

How to proceed:
- Load system modules (Python, Dask, Xarray).
- Create a custom conda environment in your project directory if needed.
- Start a Dask cluster via job submission:
  - one scheduler node  
  - N worker nodes  
- Enable the Dask dashboard on SDSC’s compute nodes.


────────────────────────────────────────
## **Step 4 — Run Parallel Raw File Loading with Dask**
Goal: Open **hundreds to thousands** of NetCDF files in parallel.

How to proceed:
- Use your Phase‑2 code with `open_mfdataset()` but now point paths to SDSC directories.
- Use chunk sizes appropriate for SDSC’s memory and CPU layout.
- Activate consolidated metadata patterns for faster open times.


────────────────────────────────────────
## **Step 5 — Distribute Spatial Regridding Across Nodes**
Goal: Regrid all chlorophyll and sea‑ice datasets onto the SST grid.

How to proceed:
- Reuse the `.interp_like()` or improved regridding from prototype.
- Submit as Dask jobs across multiple nodes.
- For each day:
  - load SST grid as reference
  - apply interpolation to CHL and ICE


────────────────────────────────────────
## **Step 6 — Perform Temporal Alignment at Scale**
Goal: Align daily SST + daily sea‑ice + 8‑day CHL composites for entire years.

How to proceed:
- Use Dask to broadcast CHL timestamps across the composite window.
- Use `.merge()` or `.interp()` on time dimension to align with SST.
- Execute this in parallel across all nodes in the cluster.


────────────────────────────────────────
## **Step 7 — Apply Global Feature Engineering at Scale**
Goal: Compute ML‑ready features across the entire global dataset.

How to proceed:
- Compute anomalies using multi‑year rolling averages.
- Add derived features (day‑of‑year, latitude, etc.).
- Apply masking where sea‑ice concentration exceeds threshold.

────────────────────────────────────────
## **Step 8 — Export Entire Cleaned Dataset to Parquet on SDSC Storage**
Goal: Produce a **Spark‑ready, ML‑ready** dataset for Phase 4.

How to proceed:
- Use Dask `.to_parquet()` with partitioning by time or region.
- Store under:
  `/project/cleaned/global_parquet/`
- Ensure partitions fit Spark’s preferred sizes (~100–200 MB per file).

────────────────────────────────────────
## **Step 9 — Verify Outputs and Document the SDSC Pipeline**
Goal: Make sure the SDSC pipeline is reliable before moving to Spark.

How to proceed:
- Inspect a few partitions locally or via Jupyter on SDSC.
- Produce quick plots:
  - global CHL map
  - SST vs CHL scatter
  - ice mask visualization
- Document each step in your README:
  - raw → regridded → aligned → engineered → parquet

────────────────────────────────────────
# **Summary**
Your Phase 3 pipeline now:

- runs on SDSC HPC resources designed for large‑scale scientific workflows 
- uses high‑speed transfer tools like Globus - processes thousands of satellite files in parallel using Dask on compute nodes  
- produces a Spark‑ready dataset stored in SDSC project storage  

You have now completed the full HPC preparation required for Phase 4 (Spark ML Pipeline).

────────────────────────────────────────



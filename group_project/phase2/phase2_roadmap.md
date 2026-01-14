#PHASE 2: Dask Prototype 
This phase transforms your Phase 1 feasibility workflow into a scalable, parallelized, multi‑file preprocessing pipeline. It is designed to run on your local machine or UCSD Datahub/DSMLP, both of which support CPU/GPU scientific workflows and installations of Python + Dask

The goal is to create a near‑production version of the pipeline you will eventually run at SDSC.

---

## Step 1: Set Up a Dask Environment
UC San Diego’s Data Science/Machine Learning Platform (DSMLP) allows you to install additional Python libraries, containers, or environments for advanced data workflows
How to proceed:

Launch a DSMLP JupyterLab session or your local environment.
Create a new environment (conda or pip) containing:
dask, distributed, xarray, netCDF4, zarr, fsspec.
Start a local Dask cluster (threads or processes).
Verify scaling by checking the Dask dashboard.

---

## Step 2: Build File Discovery and Lazy Loading
Goal: Work with many files without loading them into memory.

How to proceed:

Create a file‑list loader that scans directories:
VIIRS chlorophyll (8‑day)
OISST SST (daily)
NSIDC sea ice (daily)
Use xarray’s open_mfdataset with chunks={} to lazily load data.
Avoid loading data into RAM at this stage; rely on Dask’s on‑demand execution.

## Step 3: Construct a Regional Extraction Workflow
Goal: Now scale from a single file to hundreds of files.

How to proceed:

Define a consistent bounding box for your study region.
Apply .sel(lat=slice(a,b), lon=slice(c,d)) to each dataset.
Create small helper functions that perform consistent subsetting.

---

## Step 4: Build a Multi‑Dataset Regridding Pipeline (Dask‑powered)
Goal: Apply regridding to many files in parallel.

How to proceed:

Choose SST as the reference grid.
For each chlorophyll + sea‑ice file:
Load lazily with xarray + Dask.
Use .interp_like(sst_ds, method="linear").
Store results as Dask arrays (no compute yet).

---

## Step 5: Implement Parallel Temporal Alignment
Goal: Align chlorophyll 8‑day composites with daily SST/sea‑ice files.

How to proceed:

Extract daily timestamps from SST and sea‑ice.
Broadcast CHL timestamps to each day within the composite range.
Use Dask to join/merge datasets on time coordinates.
This allows temporal matching across hundreds of files without manually looping.

---

## Step 6: Parallel Feature Engineering
Goal: Compute predictors and targets for your ML pipeline.

How to proceed:

Compute SST anomalies using Dask operations.
Add derived features:
lat, lon, day‑of‑year, region mask.
Mask chlorophyll using sea‑ice concentration > threshold.
All transformations should occur in Dask arrays (lazy).

---

## Step 7: Convert to Partitioned Parquet Dataset
Goal: Produce a Spark‑ready dataset structure.

How to proceed:

Write the merged, cleaned dataset to Parquet using Dask.
Partition by time or region to allow scalable ML later:
dataset.to_parquet("cleaned/", partition_on=["time"])

---

## Step 8: Validate with Dask Compute + Sampling
Goal: Test whether the pipeline actually works on real data.

How to proceed:

Trigger computation on small samples using .compute().
Load a sample partition back into memory.
Plot:
chlor_a vs SST
sea‑ice fraction maps
before/after regridding maps

---

## Step 9: Document and Store in DSMLP or local repo
Goal: Document the pipeline clearly for your group.

How to proceed:

Write a Jupyter notebook describing each Dask step.
Save the notebook and scripts in GitHub.
Use DSMLP’s storage or your local directory for intermediate data.

---

## Summary
Phase 2 transforms workflow from a simple, single‑file feasibility check into a parallel, multi‑file preprocessing engine that mirrors what you will run on SDSC when you reach Phase 3. Dask is the right tool for this stage because UCSD provides research‑grade instructional environments (DSMLP, Datahub) where scalable CPU/GPU computing is supported for student projects




# Phase 2 Summary: Data Engineering & Pipeline Construction

**Status:** Complete
**Date:** Jan 2026

## 1. The Pipeline
We successfully built a scalable **ETL (Extract, Transform, Load)** pipeline using `Dask` and `xarray`.
* **Input:** Multi-agency raw files (NOAA SST, NASA Chlorophyll, NSIDC Sea Ice).
* **Processing:**
    * Lazy loading (handling data larger than RAM).
    * Spatial Regridding (aligning different resolutions to a common 0.25° grid).
    * Time Resampling (Snapping all sensors to daily averages).
* **Output:** A cloud-optimized **Zarr Store** (`ocean_analysis_jan2020.zarr`).

## 2. Key Technical Decisions
* **Zarr over NetCDF:** We switched to Zarr for the final storage. This allows parallel writing/reading and prevents "file lock" errors when using multiple Dask workers.
* **Synchronous Write:** We discovered that HDF5/NetCDF libraries are not thread-safe, causing "double free" crashes. We fixed this by forcing the final write step to be synchronous (`scheduler='sync'`).
* **Parquet for ML:** While the physical grid is stored in Zarr, we flatten the data into **Parquet** for Machine Learning. This allows Scikit-Learn to load 200k rows instantly.

## 3. Data Reality Check (The "Cloud" Issue)
* **Total Potential Pixels:** ~198,000 (31 days × 80 lat × 80 lon).
* **Valid Training Pixels:** ~13,400.
* **Why the drop?**
    * **Physics (SST):** Available 100% (Microwave sensors see through clouds).
    * **Biology (Chlorophyll):** Available ~7% (Optical sensors are blocked by clouds).
    * **Sea Ice:** Filled NaNs with `0.0` for the Hawaii region (subtropics).
* **Conclusion:** The missing data is not an error; it is a physical reality of optical satellite oceanography. The ~13k rows represent high-quality, clear-sky conditions.

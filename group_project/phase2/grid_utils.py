import numpy as np
import pyproj
import xarray as xr

def precompute_ice_indices(target_lat, target_lon, ice_proj_str):
    """
    Computes the nearest-neighbor indices to map Sea Ice (Polar Stereo)
    onto the Target Grid (Lat/Lon).
    
    Returns:
        x_ind (xr.DataArray): The x-index in the Ice grid for each Target pixel.
        y_ind (xr.DataArray): The y-index in the Ice grid for each Target pixel.
    """
    print("   [Grid Utils] Pre-computing projection indices (One-time cost)...")
    
    # 1. Setup Transformer
    transformer = pyproj.Transformer.from_crs("EPSG:4326", ice_proj_str, always_xy=True)

    # 2. Create Target Meshgrid
    lon_grid, lat_grid = np.meshgrid(target_lon, target_lat)
    
    # 3. Transform to Ice Coordinates (x, y meters)
    target_x, target_y = transformer.transform(lon_grid, lat_grid)
    
    # 4. We need to convert these projected meters (target_x) into 
    #    INTEGER array indices (0, 1, 2...) for the Ice dataset.
    #    This requires knowing the Ice Grid's x/y definition.
    #    (We will pass the Ice Dataset in the main script to do the final lookup,
    #     so here we return the raw projected coordinates).
    
    return (
        xr.DataArray(target_x, dims=("lat", "lon"), coords={"lat": target_lat, "lon": target_lon}),
        xr.DataArray(target_y, dims=("lat", "lon"), coords={"lat": target_lat, "lon": target_lon})
    )

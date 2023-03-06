# Spatial_Python
All python code for raster and vector processing


*Rasterize Vector file to raster format*

```python 
def rasterize_vector(gdf, profile, **kwargs):
    gdf = gdf.to_crs(profile['crs'])
    geoms = [g.__geo_interface__ for g in gdf.geometry.values]
    mask = rasterio.features.rasterize(
            geoms,
            out_shape=(profile['width'],profile['height']),
            transform=profile['transform'], fill= 0,
            **kwargs)
    return mask

def mask_raster_with_vector(rasterfile, vectorfile, path ):
    with rasterio.open(rasterfile) as src:
        profile = src.profile.copy()
            
    gdf = gpd.read_file(vectorfile)
   
    mask = rasterize_vector(gdf, profile)
    out_file = str(path + "rasterize.tif")
    with rasterio.open(out_file, "w", **profile) as dst:
        dst.write(mask.astype(rasterio.uint8), 1)
    
    return out_file
    
mask_raster_with_vector(rasterfile, vectorfile, path)
```

*Reclassify raster by the vector data --> rasterized file*

```python
def reclassified(raster_top, raster_down, out_dir=None):
    print(raster_top)
    with rasterio.open(raster_down) as src_down:
        data_down = src_down.read(1)
            
    # Create classification masks
    with rasterio.open(raster_top) as src_top:
        data_top = src_top.read(1)
        height, width = data_top.shape  
        profile = src_top.profile
        data = np.where(data_top==1, value_class, data_down)

    if out_dir != None:
        out_name = os.path.join(out_dir, f'reclassfied_LC.tif')
        with rasterio.open(out_name, 'w', **profile) as dst:
                dst.write(data.astype(rasterio.uint8), 1)
        
    print('Reclassified file:' + f'{out_name}')
    
    return data, out_name
```

**Together**

```python

def rasterize_vector(gdf, profile, **kwargs):
    gdf = gdf.to_crs(profile['crs'])
    geoms = [g.__geo_interface__ for g in gdf.geometry.values]
    mask = rasterio.features.rasterize(
            geoms,
            out_shape=(profile['width'],profile['height']),
            transform=profile['transform'], fill= 0,
            **kwargs)
    return mask

def mask_raster_with_vector(rasterfile, vectorfile, path ):
    with rasterio.open(rasterfile) as src_ras:
        data_down = src_ras.read(1)
        profile = src_ras.profile.copy()
            
    gdf = gpd.read_file(vectorfile)
   
    mask = rasterize_vector(gdf, profile)
    out_file = str(path + "rasterize.tif")
    with rasterio.open(out_file, "w", **profile) as dst:
        dst.write(mask.astype(rasterio.uint8), 1)
    
    # Create classification
    with rasterio.open(out_file) as src_top:
        data_top = src_top.read(1)
        height, width = data_top.shape  
        profile = src_top.profile
        data = np.where(data_top==1, value_class, data_down)
    
    out_name = os.path.join(path,f'WorldCover_{name}.tif')
      
    with rasterio.open(out_name,'w', **profile) as dst_final:
        print(data)
        dst_final.write(data.astype(rasterio.uint8), 1)
    
    return out_name
```

write single band raster

```python
def raster_file_singleband(path, rasterfile,data):
    with rasterio.open(rasterfile) as src:
        profile = src.profile.copy()
        print(profile)
    profile.update(driver="GTiff")
    with rasterio.open(str(path+"test_10.tif"), "w", **profile) as dst:
        dst.write(data.astype(rasterio.uint8), 1)
    return str(path+"test_10.tif")
```

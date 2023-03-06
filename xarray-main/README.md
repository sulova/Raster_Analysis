# xarray

### Making two plots in one
```python 
import xarray as xr
from matplotlib import pyplot as plt
import numpy as np 
fig, axs = plt.subplots(ncols=1, figsize=(20,5))

ds_hillshaded_70 = xr.load_dataset("hillshade_z70/openEO.nc")
ds_hillshaded_30 = xr.load_dataset("hillshaded_z30/openEO.nc")

ds_hillshaded_70['hillshade_mask_nan'] = ds_hillshaded_70['hillshade_mask'].where(ds_hillshaded_70['hillshade_mask'] != 0, np.nan)
ds_hillshaded_70['DEM'][1].plot.imshow(x="x", ax=axs, robust=True, cmap='viridis')
ds_hillshaded_70['hillshade_mask_nan'][1].plot.imshow(x="x", ax=axs, robust=True, cmap='autumn',alpha=1)

fig, axs = plt.subplots(ncols=1, figsize=(20,5))
ds_hillshaded_30['hillshade_mask_nan'] = ds_hillshaded_30['hillshade_mask'].where(ds_hillshaded_30['hillshade_mask'] != 0, np.nan)
ds_hillshaded_30['DEM'][1].plot.imshow(x="x", ax=axs, robust=True, cmap='viridis')
ds_hillshaded_30['hillshade_mask_nan'][1].plot.imshow(x="x", ax=axs, robust=True, cmap='autumn',alpha=1)

plt.show()
```

![image](https://user-images.githubusercontent.com/44543964/222709317-b0f00710-05e7-4458-8130-799a1f7c4008.png)

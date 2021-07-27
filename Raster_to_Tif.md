** Export raster to a .tif format

```python 
import rasterio
from matplotlib import pyplot
import numpy
import matplotlib.pyplot as plt
%matplotlib inline

# let’s read the bands using rasterio 
raster = rasterio.open('20210523_RGB.tif')

# Read the grid values into numpy arrays
red = raster.read(1)
green = raster.read(2)
blue = raster.read(3)

print("Before bands")
print(red.min(), '-', red.max(), 'mean:', red.mean())
print(green.min(), '-', green.max(), 'mean:', green.mean())
print(blue.min(), '-', blue.max(), 'mean:', blue.mean())
```
A) Normalize
```python
# Normalize bands into 0.0 - 1.0 scale
def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

# Convert to numpy arrays
red = raster.read(4)
green = raster.read(3)
blue = raster.read(2)

# Normalize band DN
nir_norm = normalize(red)
red_norm = normalize(green)
green_norm = normalize(blue)

#  Stack normaliz bands into an n-dimensional array using numpy.stack() method
nrg = numpy.dstack((nir_norm, red_norm, green_norm))

# View the color composite
plt.imshow(nrg*5)
```

B) Change band value 
```python
# Calculate for each band *10
def normal(array):
    array_new = array*10
    #array_new = array_new.astype("uint16")
    return array_new

# Normalize the bands
redbri = normal(red)
greenbri = normal(green)
bluebri = normal(blue)

print("After bands")
print(redbri.min(), '-', redbri.max(), 'mean:', redbri.mean())
print(greenbri.min(), '-', greenbri.max(), 'mean:', greenbri.mean())
print(bluebri.min(), '-', bluebri.max(), 'mean:', bluebri.mean())
```

*Save to a tif file*
```python
# Save into a tif file
rgb=rasterio.open('output.tiff', 'w', driver='Gtiff',
                          width=raster.width, height=raster.height,
                          count=3,
                          crs=raster.crs,
                          transform=raster.transform,
                          dtype='uint16')
rgb.write(redbri,1)
rgb.write(greenbri,2)
rgb.write(bluebri,3)
rgb.close()
```

import rasterio
from rasterio.windows import Window
from rasterio.transform import Affine

from shapely.geometry import box

raster1 = rasterio.open('../Data/Tree_Heights/test/S1_VV_WGS84_clip.tif')
raster2 = rasterio.open('../Data/Tree_Heights/test/S1_VH_WGS84_clip.tif')

bb_raster1 = box(raster1.bounds[0], raster1.bounds[1], raster1.bounds[2], raster1.bounds[3])
bb_raster2 = box(raster2.bounds[0], raster2.bounds[1], raster2.bounds[2], raster2.bounds[3])

print(bb_raster1)
print(bb_raster2)

xminR1, yminR1, xmaxR1, ymaxR1 = raster1.bounds
xminR2, yminR2, xmaxR2, ymaxR2 = raster2.bounds



intersection = bb_raster1.intersection(bb_raster2)
transform = Affine(raster1.res[0], 0.0, intersection.bounds[0], 0.0, -raster1.res[1], intersection.bounds[3])



p1Y = intersection.bounds[3] - raster1.res[1]/2
p1X = intersection.bounds[0] + raster1.res[0]/2
p2Y = intersection.bounds[1] + raster1.res[1]/2
p2X = intersection.bounds[2] - raster1.res[0]/2
#row index raster1
row1R1 = int((ymaxR1 - p1Y)/raster1.res[1])
#row index raster2
row1R2 = int((ymaxR2 - p1Y)/raster2.res[1])
#column index raster1
col1R1 = int((p1X - xminR1)/raster1.res[0])
#column index raster2
col1R2 = int((p1X - xminR2)/raster1.res[0])

#row index raster1
row2R1 = int((ymaxR1 - p2Y)/raster1.res[1])
#row index raster2
row2R2 = int((ymaxR2 - p2Y)/raster2.res[1])
#column index raster1
col2R1 = int((p2X - xminR1)/raster1.res[0])
#column index raster2
col2R2 = int((p2X - xminR2)/raster1.res[0])

width1 = col2R1 - col1R1 + 1
width2 = col2R2 - col1R2 + 1
height1 = row2R1 - row1R1 + 1
height2 = row2R2 - row1R2 + 1

arr_raster1 = raster1.read(1, window=Window(col1R1, row1R1, width1, height1))
arr_raster2 = raster2.read(1, window=Window(col1R2, row1R2, width2, height2))

arr_sum = arr_raster1 + arr_raster2

# Register GDAL format drivers and configuration options with a
# context manager.

with rasterio.open('../Data/Tree_Heights/test/sum3.tif',
                   'w',
                   driver='GTiff',
                   height=arr_sum.shape[0],
                   width=arr_sum.shape[1],
                   count=1,
                   dtype=arr_sum.dtype,
                   crs=raster1.crs,
                   transform=transform) as dst:

    dst.write(arr_sum, 1)

dst.close()

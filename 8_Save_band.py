import os
import rasterio


 src = rasterio.open('../Data/Tree_Heights/S2.tif)
    for band in range(1, src.count):
        single_band = src.read(band)

        # get the output name
        out_name = os.path.basename('../Data/Tree_Heights/S2.tif')
        file, ext = os.path.splitext(out_name)
        name = file + "_" + "B" + str(band) + ".tif"
        out_img = os.path.join('../Data/Tree_Heights/', name)

        print(out_img + " done")

        # Copy the metadata
        out_meta = src.meta.copy()

        out_meta.update({"count": 1})

        # save the clipped raster to disk
        with rasterio.open(out_img, "w", **out_meta) as dest:
            dest.write(single_band,1)         

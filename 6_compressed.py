dat = rasterio.open("segura/WorldCover.tif")
profile = dat.profile.copy()
profile.update(compress='lzw')

with rasterio.open("segura/WorldCover_compressed.tif", 'w', **profile) as dst:
    for ji, window in dat.block_windows(1):
        dst.write(dat.read(window=window), window=window)

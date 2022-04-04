import xarray as xr
from shapely import geometry
import matplotlib.pyplot as plt
import geopandas as gpd
import rioxarray as rioxr

def row2cell(file, x, y):
    minX = file.coords[x].min()
    maxX = file.coords[x].max()
    minY = file.coords[y].min()
    maxY = file.coords[y].max()
    poly = geometry.box(minX, minY, maxX, maxY)
    return poly

## from netCDF
in_data = xr.open_dataset('book/_temp/urban-sensors-climate_ukv/ukv_sample.nc')

a = row2cell(in_data, 'longitude', 'latitude')

bbox = gpd.GeoDataFrame(index=[0], crs={'init': 'epsg:4326'},
                        geometry=[a])
bbox.plot()
input_path = 'book/_temp/urban-sensors-climate_ukv/uk.geojson'
bbox.to_file(driver = 'GeoJSON', filename = input_path)

test = gpd.read_file(input_path)
test.plot()
plt.show()

## forest-modelling-treecrown_detectreeRGB

in_data = rioxr.open_rasterio('book/forest/modelling/forest-modelling-treecrown_detectreeRGB/output/raster/predicted_rasters_602500_646600.tif')

a = row2cell(in_data, 'x', 'y')

bbox = gpd.GeoDataFrame(index=[0], crs={'init': 'epsg:32650'},
                        geometry=[a])
bbox.plot()
plt.show()

bbox_wgs84  = bbox.to_crs({'init': 'epsg:4326'})
bbox_wgs84.plot()
plt.show()

output_path = 'book/_temp/forest-modelling-treecrown_detectreeRGB/studyarea.geojson'
bbox_wgs84.to_file(driver = 'GeoJSON', filename = output_path)

## polar-modelling-icenet
in_data = xr.open_dataset('book/polar/modelling/data/obs/siconca_EASE.nc')

a = row2cell(in_data, 'lon', 'lat')

import geopandas as gpd
bbox = gpd.GeoDataFrame(index=[0], crs={'init': 'epsg:4326'},
                        geometry=[a])
bbox.plot()
plt.show()

bbox_wgs84  = bbox.to_crs({'init': 'epsg:4326'})
bbox_wgs84.plot()
plt.show()

output_path = 'book/_temp/polar-modelling-icenet/studyarea.geojson'
bbox_wgs84.to_file(driver = 'GeoJSON', filename = output_path)
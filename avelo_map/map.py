import geopandas
import geodatasets
import contextily as cx

def generate():
    stations = geopandas.read_file("data/stations.geojson")
    ax = stations.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
    cx.add_basemap(ax, crs=stations.crs)
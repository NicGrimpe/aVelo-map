import geopandas as gpd

def visualise():
    gdf = gpd.read_file("data/Camera.geojson")
    gdf.plot()
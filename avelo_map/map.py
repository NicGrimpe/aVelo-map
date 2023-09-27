import geopandas
import contextily as cx
import folium
import json

def generate():
    stations = geopandas.read_file("data/stations.geojson")
    ax = stations.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
    cx.add_basemap(ax, crs=stations.crs)

def generate_interractive():
    m = folium.Map()
    with open("data/stations.geojson", 'r') as geo:
        a = json.load(geo)
        folium.GeoJson(a, name="stations").add_to(m)
    folium.LayerControl().add_to(m)

    m.save("output/index.html")

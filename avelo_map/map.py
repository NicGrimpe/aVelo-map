import geopandas
import contextily as cx
import folium
import json


def generate():
    stations = geopandas.read_file("data/stations.geojson")
    ax = stations.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
    cx.add_basemap(ax, crs=stations.crs)


def generate_interractive():
    m = folium.Map(location=(46.81, -71.22), zoom_start=13)
    folium.GeoJson(
        "data/stations.geojson",
        tooltip=folium.GeoJsonTooltip(fields=['Nom']),
        name="stations",
    ).add_to(m)
    folium.LayerControl().add_to(m)

    m.save("output/index.html")

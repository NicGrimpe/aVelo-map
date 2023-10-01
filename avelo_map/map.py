import folium
import json


def generate_interractive():
    m = folium.Map(location=(46.81, -71.22), zoom_start=13)
    folium.GeoJson(
        "data/stations.geojson",
        tooltip=folium.GeoJsonTooltip(fields=['Nom']),
        name="stations",
    ).add_to(m)
    folium.LayerControl().add_to(m)

    m.save("output/index.html")

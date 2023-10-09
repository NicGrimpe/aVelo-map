import folium
import json


def generate_interractive(trajets):
    m = folium.Map(location=(46.81, -71.22), zoom_start=13)
    
    folium.GeoJson(
        "data/stations.geojson",
        tooltip=folium.GeoJsonTooltip(fields=['Nom']),
        name="stations",
    ).add_to(m)
    
    # Add trajets
    for trajet in trajets:
        line = [trajet.start_coordinates, trajet.end_coordinates]
        folium.PolyLine(locations=line, weight=2, colors="#FF0000").add_to(m)

    folium.LayerControl().add_to(m)
    
    m.save("output/index.html")

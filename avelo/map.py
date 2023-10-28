import collections
import folium
import json


def generate_interractive_map(trajets):
    m = folium.Map(location=(46.81, -71.22), zoom_start=13)
    
    folium.GeoJson(
        "data/stations.geojson",
        tooltip=folium.GeoJsonTooltip(fields=['Nom']),
        name="stations",
    ).add_to(m)
    
    # Add trajets
    counter = collections.Counter((trajet.start_coordinates, trajet.end_coordinates) for trajet in trajets)
    most_common_trip = counter.most_common(1)[0][1]
    for trajet in counter:
        line = [trajet[0], trajet[1]]
        count = counter[trajet]
        folium.PolyLine(locations=line, weight=((count * 7) / most_common_trip), tooltip=f"Trip made {count} times", colors="#FF0000").add_to(m)

    folium.LayerControl().add_to(m)
    
    m.save("output/index.html")

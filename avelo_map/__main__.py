from avelo_map.extraction import extract
from avelo_map import trajet, map
import folium
import geojson

if __name__ == "__main__":
    
    f = open('data/stations.geojson')
    stations = geojson.load(f)
    
    trajets = extract('data/mes-trajets.txt')
    for t in trajets:
        unTrajet = trajet.trajet_from_regex_extraction(t)

    #map.generate_interractive()

from avelo_map.extraction import extract
from avelo_map import trajet, map, stations
import folium
import geojson

if __name__ == "__main__":

    avelo_stations = stations.Stations()

    trajets = extract('data/mes-trajets.txt')
    for t in trajets:
        a = trajet.trajet_from_regex_extraction(t)
        a.add_coordinates(avelo_stations.stations)
        print(a)

    #map.generate_interractive()

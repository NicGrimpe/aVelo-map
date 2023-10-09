from avelo_map.trajets_extraction import extract_from_file
from avelo_map.trajet import trajet_from_regex
from avelo_map import map, stations
import folium
import geojson

if __name__ == "__main__":

    avelo_stations = stations.Stations()

    trajets = []
    regexed_trajets = extract_from_file('data/all-trajets.txt')
    for regex_trajet in regexed_trajets:
        trajet = trajet_from_regex(regex_trajet)
        trajet.add_coordinates(avelo_stations.stations)
        trajets.append(trajet)

    print(f"Tu as fait {len(trajets)} trajets!")
    map.generate_interractive(trajets)

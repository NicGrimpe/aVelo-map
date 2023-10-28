from avelo.trajets_extraction import fetch_for_year
from avelo import map, stations

if __name__ == "__main__":
    avelo_stations = stations.Stations()
    trajets = fetch_for_year(2023)
    for t in trajets:
        t.add_coordinates(avelo_stations.stations)
    print(f"Tu as fait {len(trajets)} trajets!")
    map.generate_interractive_map(trajets)

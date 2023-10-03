import geojson

class Stations():
    def __init__(self, path='data/stations.geojson'):
        self.stations = self.__extract_stations(path) 

    def __extract_stations(self, file_path):
        f = open(file_path)
        raw_stations = geojson.load(f)

        stations = {}
        for station in raw_stations["features"]:
            station_name = station["properties"]["Nom"]
            station_coordinates = station["geometry"]["coordinates"]
            stations[station_name] = station_coordinates
        
        return stations

    def __str__(self):
        return str(self.stations)

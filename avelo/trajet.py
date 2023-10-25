def trajet_from_regex(regexed_trajet):
    return Trajet(
        regexed_trajet[0], regexed_trajet[2], regexed_trajet[3], regexed_trajet[4]
    )

class UnknownStationException(Exception):
    pass

class Trajet:
    def __init__(self, start_time, end_time, start_station, end_station) -> None:
        self.start_time = start_time
        self.start_station = start_station
        self.end_time = end_time
        self.end_station = end_station

        self.start_coordinates = None
        self.end_coordinates = None

    def add_coordinates(self, stations):
        if self.start_station in stations.keys():
            self.start_coordinates = stations[self.start_station]
        else:
            raise UnknownStationException(f"Station '{self.start_station}' unknown")

        if self.end_station in stations.keys():
            self.end_coordinates = stations[self.end_station]
        else:
            raise UnknownStationException(f"Station '{self.end_station}' unknown")

    def __str__(self) -> str:
        return f"{self.start_station} ({self.start_coordinates}) -> {self.end_station} ({self.end_coordinates})"

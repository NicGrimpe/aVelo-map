
def trajet_from_regex_extraction(regexed_trajet):
    return Trajet(regexed_trajet[0], regexed_trajet[2], regexed_trajet[3], regexed_trajet[4])

class Trajet():
    def __init__(self, start_time, end_time, start_location, end_location) -> None:
        self.start_time = start_time
        self.start_location = start_location
        self.end_time = end_time
        self.end_location = end_location

    def __str__(self) -> str:
        return f"{self.start_location} -> {self.end_location}"
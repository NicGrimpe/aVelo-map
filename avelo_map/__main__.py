from avelo_map.extraction import extract
from avelo_map import trajet, map
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # trajets = extract('data/mes-trajets.txt')
    # for t in trajets:
    #     unTrajet = trajet.trajet_from_regex_extraction(t)
    #     print(unTrajet)
    map.generate()
    plt.show()

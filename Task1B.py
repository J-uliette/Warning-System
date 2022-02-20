
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()
    lists = stations_by_distance(stations, (52.2053, 0.1218))
    print("the closest 10 stations are")
    print(lists[:10])
    print("the farther 10 stations are")
    print(lists[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
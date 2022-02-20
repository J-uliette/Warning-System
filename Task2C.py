from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()

    update_water_levels(stations)

    highest_stations = stations_highest_rel_level(stations, 10)

    for i in range (len(highest_stations)):
        print (highest_stations[i][0].name + ' ' + str(highest_stations[i][1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

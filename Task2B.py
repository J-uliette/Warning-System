from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():

    stations = build_station_list()

    update_water_levels(stations)

    stations_over = stations_level_over_threshold(stations, 0.8)
    

    for i in range (len(stations_over)):
        print (str(stations_over[i][0].name) + ' ' + str(stations_over[i][1]))

    print (type(stations_over[0]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
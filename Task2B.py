from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

update_water_levels(stations)


for i in range (len(stations)):
    print(stations[i].relative_water_level()) 




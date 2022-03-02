from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

update_water_levels(stations)
severe = []
high = []
moderate = []
low = []
stations_over = stations_level_over_threshold(stations, 1)
for i in range(len(stations_over)):
    if stations_over[i][1] >= 3:
        severe.append(stations_over[i])
    elif stations_over[i][1] >= 2:
        high.append(stations_over[i])
    elif stations_over[i][1] >= 1.5:
        moderate.append(stations_over[i])
    else:
        low.append(stations_over[i])
print(low)
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import towns_from_MonitoringStation as townget
stations = build_station_list()

update_water_levels(stations)
severe = []
high = []
moderate = []
low = []
stations_over = stations_level_over_threshold(stations, 1)
for i in range(len(stations_over)):
    if stations_over[i][1] >= 3:
        severe.append((stations_over[i][0].town, stations_over[i][0].latest_level))
    elif stations_over[i][1] >= 2:
        high.append((stations_over[i][0].town, stations_over[i][0].latest_level))
    elif stations_over[i][1] >= 1.5:
        moderate.append((stations_over[i][0].town, stations_over[i][0].latest_level))
    else:
        low.append((stations_over[i][0].town, stations_over[i][0].latest_level))

print("The most at risk stations are:" + str(severe))
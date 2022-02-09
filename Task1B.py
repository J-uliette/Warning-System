
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
lists = stations_by_distance(stations, (52.2053, 0.1218))
print("the closest 10 stations are")
print(lists[:10])
print("the farther 10 stations are")
print(lists[-10:])
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

centre_coord = (52.2053, 0.1218) #Cambridge city centre coord
radius_km = 10 #radius of data included
station_list = build_station_list()

within_radius_list = stations_within_radius(station_list, centre_coord, radius_km) #unsorted list of MonitoringStation classes

just_names = []

for i in range(len(within_radius_list)):
    just_names.append(within_radius_list[i].name)

sorted_names = sorted(just_names)

print (sorted_names)
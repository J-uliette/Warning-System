from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


centre_coord = (52.2053, 0.1218) #Cambridge city centre coord
radius_km = 10 #radius of data included


within_radius = stations_within_radius(build_station_list, centre_coord, radius_km)

print (within_radius)

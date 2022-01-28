from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

from floodsystem.utils import sorted_by_key

centre_coord = (52.2053, 0.1218) #Cambridge city centre coord
radius_km = 10 #radius of data included
station_list = build_station_list()

within_radius = stations_within_radius(station_list, centre_coord, radius_km)

print (sorted_by_key(within_radius, 0))

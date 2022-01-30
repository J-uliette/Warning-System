from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.utils import names_from_MonitoringStation as nameGet
from floodsystem.stationdata import build_station_list

stations = build_station_list()

inconsistent_stations = inconsistent_typical_range_stations(stations)

print (nameGet(inconsistent_stations))

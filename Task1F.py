from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.utils import names_from_MonitoringStation as nameGet
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    print (nameGet(inconsistent_stations))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
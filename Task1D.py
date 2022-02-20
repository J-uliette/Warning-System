from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.utils import names_from_MonitoringStation as nameGet

def run():

    stations = build_station_list()

    rivers = rivers_with_station(stations)

    river_dict = stations_by_river(stations)


    print (str(len(rivers)) + ' rivers have at least one monitoring station. First 10 - ' + str(rivers[0:10]))

    print(nameGet(river_dict['River Aire']))
    print(nameGet(river_dict['River Cam']))
    print(nameGet(river_dict['River Thames']))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
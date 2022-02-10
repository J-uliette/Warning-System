"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def test_stations_within_radius():
    stations = build_station_list()
    in_radius = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(in_radius) == 11

def test_rivers_with_station():
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    assert rivers[0] < rivers[1]
    assert len(rivers) < len(stations)
    assert rivers[0] not in rivers[1:]

def test_stations_by_river():
    stations = build_station_list()
    dictionary = geo.stations_by_river(stations)
    assert type(dictionary) == dict
    assert 'River Cam' in dictionary

def test_stations_by_distance():
    stations = build_station_list()

    p = (51.47, -0.609)
    sorted_stations = geo.stations_by_distance(stations, p)
    assert len(stations) == len(sorted_stations)
    for i in range(len(stations) - 1):
       assert sorted_stations[i][2] <= sorted_stations[i + 1][2]
def test_rivers_by_station_number():
    #Build list of stations
    stations = build_station_list()
    N = 5
    
    #Get results of rivers
    rivers_station_number = geo.rivers_by_station_number(stations, N)
    assert len(rivers_station_number) >= N
    N = 9
    
    #Get results of rivers
    rivers_station_number = geo.rivers_by_station_number(stations, N)
    assert len(rivers_station_number) >= N
    
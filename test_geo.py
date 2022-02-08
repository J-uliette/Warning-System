"""Unit test for the geo module"""
import types
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
    
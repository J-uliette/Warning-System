"""Unit test for the geo module"""
from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo


def test_stations_within_radius():
    stations = build_station_list()
    in_radius = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(in_radius) == 11
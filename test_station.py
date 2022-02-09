# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    inconsistentRange = (2.3, -3.4445)
    NoneRange = None
    consistentRange = (-0.3, 4.7)
    river = "River X"
    town = "My Town"
    inconsistentStation =  MonitoringStation(s_id, m_id, label, coord, inconsistentRange, river, town)
    NoneStation =  MonitoringStation(s_id, m_id, label, coord, NoneRange, river, town)
    consistentStation =  MonitoringStation(s_id, m_id, label, coord, consistentRange, river, town)
    assert consistentStation.typical_range_consistent() == True
    assert inconsistentStation.typical_range_consistent() == False
    assert NoneStation.typical_range_consistent() == False

def test_inconsistent_typical_range_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    inconsistentRange = (2.3, -3.4445)
    inconsistentRangeNone = None
    consistentRange = (-0.3, 4.7)
    river = "River X"
    town = "My Town"
    inconsistentStation =  MonitoringStation(s_id, m_id, label, coord, inconsistentRange, river, town)
    inconsistentNoneStation =  MonitoringStation(s_id, m_id, label, coord, inconsistentRangeNone, river, town)
    consistentStation =  MonitoringStation(s_id, m_id, label, coord, consistentRange, river, town)
    stations = [inconsistentStation, inconsistentNoneStation, consistentStation]
    assert inconsistentStation in inconsistent_typical_range_stations(stations)
    assert inconsistentNoneStation in inconsistent_typical_range_stations(stations)
    assert consistentStation not in inconsistent_typical_range_stations(stations)
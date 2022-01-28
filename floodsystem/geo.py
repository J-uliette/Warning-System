# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
'''from . import utils'''
from .utils import sorted_by_key  # noqa'''
 #'ImportError: attempted relative import with no known parent package' as an error

from haversine import haversine, Unit

def stations_by_distance(stations, p): #1B
        distance = []
        names = []
        towns = []
        for item in stations:
            dist = haversine(item.coord, p)
            distance.append(dist)
        for item in stations:
            names.append(item.name)
        for item in stations:
            towns.append(item.town)
        finaldistancelist = list(zip(names, towns, distance))
        finaldistancelist.sort(key=lambda x:x[2])
        return finaldistancelist[:10], finaldistancelist[-10:]

def stations_within_radius(stations, centre, r): #1C

    within_radius = []
    
    for station in stations:
        distance = haversine(centre, station.coord)
        if distance <= r:
            within_radius.append(station)
    
    return within_radius

def rivers_with_station(stations): #1D
    '''returns a set of rivers with stations
    {'Ganges', 'Nile', 'Amazon'} etc'''

    
    rivers = set() #empty set to put rivers with stations into
    for station in stations:
         rivers.add(station.river)

    return rivers

def stations_by_river(stations):
    '''returns a dictionary that maps river names (the 'key') to a list of station objects on a given river'''
    dictionary = {}
    for station in stations:
        list_stations_on_river = []
        dictionary[station.river] = station.name

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import utils  #below wasn't working so now need to do utils.function() 
#from .utils import sorted_by_key
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
    '''Returns a list (unsorted) of all stations within a radius
    r from a centre coordinate'''

    within_radius = []
    
    for station in stations:
        distance = haversine(centre, station.coord) #calculates distance using haversine
        if distance <= r:
            within_radius.append(station)
    
    return sorted(within_radius)

def rivers_with_station(stations): #1D
    '''returns a sorted set of rivers with stations
    {'Ganges', 'Nile', 'Amazon'} etc'''

    
    rivers = set() #empty set to put rivers with stations into
    for station in stations:
         rivers.add(station.river)

    return sorted(rivers)

def stations_by_river(stations):
    """returns a dictionary that maps river names (the 'key') to a list of station objects on a given river
    {'Cam':[Station1, Station2]} where StationX is the MonitoringStation class"""

    dictionary = {}
    rivers = rivers_with_station(stations) #gets a list of rivers to find stations on

    for i in range (len(rivers)): #iterating across all rivers
        stations_on_river = []    #empties the list after the ith river iteration

        for station in stations:  #iterates across all stations and looks if the river matches

            if rivers[i] == station.river:
                stations_on_river.append(station)

        dictionary[str(rivers[i])] = stations_on_river #adds the station list 
    
    return dictionary

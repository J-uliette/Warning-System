# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key # noqa
from haversine import haversine, Unit
'''import plotly.express as px'''

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
        return finaldistancelist

def stations_within_radius(stations, centre, r): #1C
    '''Returns a list (unsorted) of all stations (type MonitoringStation) within a radius
    r from a centre coordinate'''

    within_radius = []
    
    for station in stations:
        distance = haversine(centre, station.coord) #calculates distance using haversine
        if distance <= r:
            within_radius.append(station)
    
    return within_radius

def rivers_with_station(stations): #1D
    '''returns a sorted set of rivers with stations
    eg {'Amazon', 'Euphrates', 'Ganges', 'Nile', 'Zambezi'}'''

    
    rivers = set() #empty set to put rivers with stations into
    for station in stations:
         rivers.add(station.river)

    return sorted(rivers)

def stations_by_river(stations): #1D
    """returns a dictionary that maps river names (the 'key') to a list of station objects on a given river
    {'River Cam':[Station1, Station2]} where StationX is the MonitoringStation class"""

    dictionary = {}
    rivers = rivers_with_station(stations) #gets a list of rivers to find stations on

    for i in range (len(rivers)): #iterating across all rivers
        stations_on_river = []    #empties the list after the ith river iteration

        for station in stations:  #iterates across all stations and looks if the river matches

            if rivers[i] == station.river:
                stations_on_river.append(station)

        dictionary[str(rivers[i])] = stations_on_river #adds the station list 
    
    return dictionary

def rivers_by_station_number(stations, N): #1E
    "determines the N rivers with the greatest number of monitoring stations." 
    "It should return a list of (river name, number of stations) tuples, sorted "
    "by the number of stations. In the case that there are more rivers with the "
    "same number of stations as the N th entry, include these rivers in the list. "
    rivers = rivers_with_station(stations)
    riverslist = [] #empty river list
    listrivernumber = [] #create final empty list for river name and number of stations
    for x in stations:
        riverslist.append(x.river) #get river list with repetition
    for y in rivers:
        occurence = riverslist.count(y) #count number of times each river comes up
        tuples = (y, occurence)
        listrivernumber.append(tuples) #create list
    listrivernumber.sort(key=lambda x:x[1]) #sort by second elemnt of tuple
    endlist = listrivernumber [-N:]
    for i in range(1,900):
        if listrivernumber[-N-i][1] == listrivernumber[-N][1]:
            endlist.insert(0,listrivernumber[-N-i])
    return endlist


'''def plot_stations(stations):

    px.set_mapbox_access_token(open(".mapbox_token").read())

    fig = px.scatter_mapbox(stations,
                        lat=stations.coord[0],
                        lon=stations.coord[1],
                        hover_name=stations.name,
                        zoom=1)
    fig.show()'''

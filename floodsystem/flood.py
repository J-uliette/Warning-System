from floodsystem.stationdata import update_water_levels
from .utils import sorted_by_key
from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol): #2B
    '''Returns a list of tuples, where each tuple holds 
    (i) a station (object) at which the latest relative 
    water level is over tol and (ii) the relative water 
    level at the station. It is sorted in descending 
    order of relative water levels'''

    stations_over = [] #empty list


    for station in stations: #iterating across all stations
        if (type(station.latest_level) == float)  and (station.typical_range_consistent() == True): #excludes NoneType and makes sure the range is consistent
            if (station.relative_water_level() > tol) and (station.relative_water_level() < 50): #makes sure relative water level isn't ridiculously high (Letcombe Basset lol)
                stations_over.append((station, station.relative_water_level())) #adds station to the list
    

    sorted_stations = sorted_by_key(stations_over, 1, True) #sorts by relative water level in descending order

    return (sorted_stations)


def stations_highest_rel_level(stations, N):
    '''returns a list of the N stations (objects) 
    at which the water level, relative to the typical 
    range, is highest. The list is sorted in 
    descending order by relative level.'''
            
    stations_over = stations_level_over_threshold(stations, -1000) #tolerance is sufficiently (negatively) large to include every station

    highest_stations = stations_over[:N] #slices from [0] up to [N]

    sorted_stations = sorted_by_key(highest_stations, 1, True)
    #unnecessary as long as the stations_level_over_threshold works as it should
    
    return sorted_stations

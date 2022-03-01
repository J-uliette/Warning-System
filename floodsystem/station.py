# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self): #1F
        if self.typical_range == None:
            return False
        else:
            return (self.typical_range[0] < self.typical_range[1]) #returns True if lowest level (index 0) is actually lower of the two

    def relative_water_level(self): #2B
        '''NEEDS UPDATED WATER LEVELS
        Returns fraction from 0 to 1 of value. Does this by dividing the 
        difference of the latest value and the typical lowest value, by the range.
        If the typical range data is inconsistent, returns None '''

        if self.typical_range_consistent() == False:
            return None
        elif self.latest_level == None:  #IF THE WATER LEVELS HAVEN'T BEEN UPDATED THIS WILL ALWAYS BE NONE
            print('Update the water levels first maybe?')
            return None
        else:
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])


def inconsistent_typical_range_stations(stations): #1F
    '''returns a list (MonitoringStation objects) of 
    stations with inconsistent typical range data'''
    
    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station)
    return inconsistent_stations

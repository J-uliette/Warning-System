# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1)], 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1)], 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def names_from_MonitoringStation(stations):
  '''returns a sorted list of station names where the parameter (stations)
  is a list of MonitoringStation objects'''

  names = []

  for station in stations:
    names.append(station.name)
  
  return sorted(names)

def towns_from_MonitoringStation(stations):
  '''returns a sorted list of station towns where the parameter (stations)
  is a list of MonitoringStation objects'''

  towns = []

  for station in stations:
    towns.append(station.town)
  
  return sorted(towns)
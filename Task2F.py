from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

N=5
p=4
dt = 2 #parameters
stations = build_station_list() #build list of stations
finallist = stations_highest_rel_level(stations, N) #get 5 highest risk stations
for i in range(len(finallist)): #iterate over 5 stations
    dates, levels = fetch_measure_levels(finallist[i].measure_id,
                                     dt=datetime.timedelta(days=dt)) #get the dates and levels
    plot_water_level_with_fit(finallist[i], dates, levels, p)
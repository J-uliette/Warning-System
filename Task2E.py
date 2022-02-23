import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
stations = build_station_list()
stationlist=stations_highest_rel_level(stations, 5)
dt = 10
for i in range(len(stationlist)):
    dates, levels = fetch_measure_levels({}.measure_id,dt=datetime.timedelta(days=dt)).format(stationlist[i])
    plot_water_levels(stationlist[i],dates,levels)
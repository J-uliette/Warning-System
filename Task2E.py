from matplotlib import pyplot as plt
from datetime import datetime, timedelta, date
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
stations = build_station_list()
update_water_levels(stations)
stationlist=stations_highest_rel_level(stations, 5)
dt = 10


for i in range(len(stationlist)):
    dates, levels = fetch_measure_levels(stationlist[i][0].measure_id,dt)
    plot_water_levels(stationlist[i],dates,levels)

#print (stationlist)
#print (fetch_measure_levels(stationlist[1].measure_id,dt=datetime.timedelta(days=dt)).format(stationlist[1]))

# Plot
'''plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
plt.xlabel('date')
plt.ylabel('water level (m)')
plt.xticks(rotation=45);
plt.title(station)

# Display plot
plt.tight_layout() 

plt.show()'''
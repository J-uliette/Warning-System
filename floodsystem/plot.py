import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    plot_water_levels(station, dates, levels)
    polyfit(dates, levels, p)
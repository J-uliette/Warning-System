import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date

def polyfit(dates, levels, p):# Create set of 10 data points on interval (1000, 1002)
    x = dates
    y = levels

    d0 = len(dates) 
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
    # Display plot
    #plt.show()
    return poly, d0
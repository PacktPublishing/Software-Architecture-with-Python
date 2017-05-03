# Code Listing #2
"""

Plot graphs of performance counters 

"""

import matplotlib.pyplot as plt

def plot(xdata, ydata):
    """ Plot a range of ydata (on y-axis) against xdata (on x-axis) """
    
    plt.plot(xdata, ydata)
    plt.show()

def plot_many(xdata, ydatas):
    """ Plot a sequence of ydatas (on y-axis) against xdata (on x-axis) """
    
    for ydata in ydatas:
        plt.plot(xdata, ydata)
    plt.show()


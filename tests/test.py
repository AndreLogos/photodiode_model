"""Module for testing."""
import csv
import os
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

def equally_sized_curves(curve1:list, curve2:list, dx:float, limits:tuple) -> tuple:
    """
    Make two new curves with the same length and with X axis equally spaced. The  interval of the new curves is dx. The values completed if dx of given curves are greater than dx considers that between two points of the data the curve is linear.
    """
    samples = int((limits[1] - limits[0])/dx)
    x1 = curve1[0]
    y1 = curve1[1]
    x2 = curve2[0]
    y2 = curve2[1]
    new_x = np.linspace(limits[0], limits[1], num=samples)
    new_y1 = np.linspace(0, 0, num=samples)
    new_y2 = np.linspace(0, 0, num=samples)
    c1_index = 0 # Index for iterate over each curve 
    c2_index = 0 # Index for iterate over each curve
    for i, x in enumerate(new_x):
        # Finding a value of x between two points of curves 1 and 2 
        while x1[c1_index+1] < x:
            c1_index += 1
        while x2[c2_index+1] < x:
            c2_index += 1

        a1 = (y1[c1_index+1]-y1[c1_index])/(x1[c1_index+1]-x1[c1_index])
        b1 = y1[c1_index] - a1*x1[c1_index]
        new_y1[i] = a1*x + b1

        a2 = (y2[c2_index+1]-y2[c2_index])/(x2[c2_index+1]-x2[c2_index])
        b2 = y2[c2_index] - a2*x2[c2_index]
        new_y2[i] = a2*x + b2

    new_curve1 = [new_x,new_y1]
    new_curve2 = [new_x,new_y2]
    return new_curve1, new_curve2


x1 = [-1,0,1,2,3,4,5,6,7,8,9,10]
y1 = [0,1,2,3,4,5,6,7,8,9,10,11]

x2 = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
y2 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

curve1 = [np.array(x1), np.array(y1)]
curve2 = [np.array(x2), np.array(y2)]
limits = (0, 10)

_, ax1 = plt.subplots()
ax1.scatter(x1, y1)
ax1.scatter(x2, y2)
ax1.set_xticks(np.arange(-2, 13, 0.1), minor=True)
ax1.grid()

newcurve1, newcurve2 = equally_sized_curves(curve1, curve2, 0.1, limits)
_, ax2 = plt.subplots()
ax2.scatter(newcurve1[0], newcurve1[1])
ax2.scatter(newcurve2[0], newcurve2[1])
ax2.set_xticks(np.arange(-2, 13, 0.1), minor=True)
ax2.grid()

plt.show()

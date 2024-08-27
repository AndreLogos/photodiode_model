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
    new_curve1 = [0,0]
    new_curve2 = [0,0]
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

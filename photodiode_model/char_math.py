"""Module to do math operations with models characterístics"""

import numpy as np

def common_limits(x_axis1:np.ndarray, x_axis2:np.ndarray) -> tuple:
    """
    Returns the limits that both curves of the characteristics has data. If the return is 0 for both limits the curves has no common section to multiply or divide the data.

    Parameters:
        x_axis1 (np.ndarray): One X axis data.
        x_axis2 (np.ndarray): Another X axis data.

    Returns:
        tuple (tuple):
            - bottom_limit (float): The highest bottom limit
            - top_limit (float): The lowest top limit
    """
    if x_axis1[0] >= x_axis2[0]:
        bottom_limit = x_axis1[0]
    else:
        bottom_limit = x_axis2[0]
    if x_axis1[-1] <= x_axis2[-1]:
        top_limit = x_axis1[-1]
    else:
        top_limit = x_axis2[-1]
    if bottom_limit >= top_limit:
        return 0, 0
    else:
        return bottom_limit, top_limit


def equally_sized_curves(curve1:list, curve2:list, dx:float, limits:tuple) -> tuple:
    """
    Make two new curves with the same length and with X axis equally spaced. The  interval of the new curves is dx. The values completed if dx of given curves are greater than dx considers that between two points of the data the curve is linear.

    Parameters:
        curve1 (list): List of two numpy arrays representing the axes of the curve, the first element is the X axis, the second element is the Y axis.
        curve2 (list): List of two numpy arrays representing the axes of the curve, the first element is the X axis, the second element is the Y axis.
        dx (float): Desired space between two adjacent values of the new X axis.
        limits (tuple): Tuple with Bottom and Top values of the new X axis.

    Returns:
        tuple (tuple):
            - list of two numpy arrays representing the new curve 1
            - list of two numpy arrays representing the new curve 2
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


def multiply(characteristic1:tuple, characteristic2:tuple, dx:float) -> tuple:
    """
    Multiply two characteristic curves. The characteristic dict data must be:
        - "Name" (string): The name of the curve.
        - "x_axis" (np.ndarray): X axis data.
        - "y_axis" (np.ndarray): Y axis data.
    
    Only the data present in both curves simultaneously are multiplied, the rest is considered to be multiplied by zero, since exists only in one curve.

    Parameters:
        characteristic1 (dict): A dictionary of one datasheet curve.
        characteristic2 (dict): A dictionary of another datasheet curve.
        dx (float): Desired space between new X axis adjacent values of the resulting curve.
        
    Returns:
        tuple (tuple):
            - x_axis (np.ndarray): X axis data.
            - y_axis (np.ndarray): Y axis data. 
    """
    limits = common_limits(characteristic1[1], characteristic2[1])
    curve1 = [characteristic1[1], characteristic1[2]]
    curve2 = [characteristic2[1], characteristic2[2]]
    new_curve1, new_curve2 = equally_sized_curves(curve1, curve2, dx, limits)
    return (new_curve1[0], new_curve1[1]*new_curve2[1])

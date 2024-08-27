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


def equally_sized_curves(curve1:list, curve2:list, limits:tuple):
    """
    Make two new curves with the same length and with X axis equally spaced. The  interval of the new curves is 0.001. The values completed if dx of given curves are greater than 0.001 considers that between two points of the data the curve is linear.
    """


def multiply(characteristic1:dict, characteristic2:dict) -> tuple:
    """
    Multiply two characteristic curves. The characteristic dict data must be:
        - "Name" (string): The name of the curve.
        - "x_axis" (np.ndarray): X axis data.
        - "y_axis" (np.ndarray): Y axis data.
    
    Only the data present in both curves simultaneously are multiplied, the rest is considered to be multiplied by zero, since exists only in one curve.

    Parameters:
        characteristic1 (dict): A dictionary of one datasheet curve.
        characteristic2 (dict): A dictionary of another datasheet curve.
        
    Returns:
        tuple (tuple):
            - x_axis (np.ndarray): X axis data.
            - y_axis (np.ndarray): Y axis data. 
    """
    limits = common_limits(characteristic1['x_axis'], characteristic2['x_axis'])
    curve1 = [characteristic1['x_axis'], characteristic1['y_axis']]
    curve2 = [characteristic2['x_axis'], characteristic2['y_axis']]
    data = equally_sized_curves(curve1, curve2, limits)
    
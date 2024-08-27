"""Module to define Photodetectors components."""

import csv
import os
import numpy as np

class Photodiode():
    """
    Class to define a Photodiode.
        
    Attributes:
        efective_area (float):  Radiant sensitive area (in mm2).
        reverse_voltage (float): Operational Reverse voltage.
        __characteristics (list): Characteristics curves from the datasheet.
    """
    def __init__(self, efective_area : float, reverse_voltage : float):
        """
        Constructs the basics attributes of a Photodiode.

        Parameters:
            efective_area (float):  Radiant sensitive area (in mm2).
            reverse_voltage (float): Operational Reverse voltage.

        Also creates an empty list of Photodiode characteristics curves of its datasheet. The characteristics curves are Dictionaries with: Name, X axis data and Y axis data.
        """
        self.efective_area = efective_area
        self.reverse_voltage = reverse_voltage
        self.__characteristics = []

    def add_char(self, name : str, x_axis : np.ndarray, y_axis : np.ndarray):
        """
        Add a curve of a characteristic from the photodiode datasheet.

        Parameters:
            name (str): Name of the characteristic curve.
            x_axis (np.ndarray): X axis of the curve.
            y_axis (np.ndarray): Y axis of the curve.

        Returns:
            None (None): Has no returns.
        """
        dict_caracteristic = {
                "Name" : name,
                "x_axis" : x_axis,
                "y_axis" : y_axis
            }
        self.__characteristics.append(dict_caracteristic)

    def add_char_from_csv(self, filepath : str):
        """
        Add a curve of a characteristic from the photodiode datasheet.
        
        Parameters:
            filepath (str): Path to the csv file with the X and Y data points, the first column is the X data and the second column is the Y data.

        Returns:
            None (None): Has no returns.
        """
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            name = os.path.basename(filepath)
            name = name.removesuffix('.csv')
            data = list(csv.reader(csvfile))
        x_axis = np.array([])
        y_axis = np.array([])
        for _, axis in enumerate(data):
            x_axis = np.append(x_axis, float(axis[0]))
            y_axis = np.append(y_axis, float(axis[1]))
        dict_caracteristic = {
        "Name" : name,
        "x_axis" : x_axis,
        "y_axis" : y_axis
        }
        self.__characteristics.append(dict_caracteristic)

    def get_char(self, name : str) -> tuple:
        """
        Returns the data of a characteristic curve:

        Parameters:
            name (str): Name of the curve.

        Returns:
            tuple(tuple):
                - name (str): Name of the curve.
                - x_axis (np.ndarray): X axis data points.
                - y_axis (np.ndarray): Y axis data points.
        """
        found = False
        for _, characteristic in enumerate(self.__characteristics):
            if characteristic["Name"] == name:
                found = True
                return (characteristic["Name"],
                        characteristic["x_axis"],
                        characteristic["y_axis"])
        if not found:
            print("Characteristic not found. Available characteristics:")
            self.characteristics()
            return None, None, None


    def rm_char(self, name : str):
        """
        Removes a characteristic.
                 
        Parameters:
            name (str): Name of the curve.

        Returns:
            None (None): Has no returns.
        """
        found = False
        for i, characteristic in enumerate(self.__characteristics):
            if characteristic["Name"] == name:
                self.__characteristics.remove(i)
                found = True
        if not found:
            print("Characteristic not found. Available characteristics:")
            self.characteristics()

    def integrate_char(self, name : str) -> float:
        """
        Integrates a characteristic of the phtodetector. Uses trapezoidal integration.
        
        Parameters:
            name (str): Name of the curve.
        
        Returns:
            curves_area (float): Area of the curve.
        """
        _, x_axis, y_axis = self.get_char(name=name)
        if x_axis is None:
            return 0
        else:
            return np.trapezoid(
                y=y_axis,
                x=x_axis)

    def characteristics(self):
        """Prints all characteristics added of the photodiode."""

        for _, char in enumerate(self.__characteristics):
            print( char["Name"])

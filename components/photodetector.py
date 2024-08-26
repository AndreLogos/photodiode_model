"""Class to define the Photodetector component."""
import csv

import pandas as pd
import numpy as np

class Photodetector():
    """Class to define the Photodetector"""
    def __init__(self, efective_area : float, reverse_voltage : float):
        self.efective_area = efective_area
        self.reverse_voltage = reverse_voltage
        self.__characteristics = []

    def add_char(self, name : str, x_axis : np.ndarray, y_axis : np.ndarray):
        """Adding a graphic of a characteristic from the
            photodetector datasheet."""
        dict_caracteristic = {
                "Name" : name,
                "x_axis" : x_axis,
                "y_axis" : y_axis
            }
        self.__characteristics.append(dict_caracteristic)

    def add_char_from_csv(self, filename : str):
        """Adding a graphic of a characteristic from the
            photodetector datasheet."""
        with open(filename, newline='', encoding='utf-8') as csvfile:
            data = list(csv.reader(csvfile))


    def get_char(self, name : str) -> tuple:
        """Returns a dictionary of characteristic:
            "Name": str, "x_axis": np.ndarray, "y_axis": np.ndarray
        """
        found = False
        for i in enumerate(self.__characteristics):
            if self.__characteristics[i]["Name"] == name:
                found = True
                return (self.__characteristics[i]["Name"],
                        self.__characteristics[i]["x_axis"],
                        self.__characteristics[i]["y_axis"])
        if not found:
            print("Characteristic not found.")
            return None, None, None


    def rm_char(self, name : str):
        """Removes a characteristic."""
        found = False
        for i in enumerate(self.__characteristics):
            if self.__characteristics[i]["Name"] == name:
                self.__characteristics.remove(i)
                found = True
        if not found:
            print("Characteristic not found.")

    def integrate_char(self, name : str, dx : float) -> float:
        """Integrates a characteristic of the phtodetector.
            Uses trapezoidal integration with given dx."""
        _, y_axis, x_axis = self.get_char(name=name)
        if y_axis is None:
            return 0
        else:
            return np.trapezoid(
                y_axis,
                x_axis,
                dx=dx)

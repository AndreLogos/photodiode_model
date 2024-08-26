"""Module for testing."""
import csv
import pandas as pd

filename = "../components/photodetector_curves/relative_spectral_sensitivity_x_wavelength.csv"
with open(filename, newline='', encoding='utf-8') as csvfile:
    data = list(csv.reader(csvfile))

print(data)
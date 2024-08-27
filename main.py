"""Module to estimate Photodiode currente based on the Photodiode and Light source caracteristics"""
from pathlib import Path

import numpy as np

from photodiode_model.light_source import LightSource
from photodiode_model.photodetector import Photodiode

root_path = Path(__file__).parent

BPW21R = Photodiode(efective_area=7.5, reverse_voltage=0)
MH_100 = LightSource(power=100, luminous_flux=3000)


def main():
    """Main function."""
    # Photodiode = pd and light source = ls

    pd_sensibility = root_path/'data'/'photodetector_curves'/'relative_sensitivity_x_wavelength.csv'
    ls_sensibility = root_path /'data'/'light_source_curves'/'relative_output_x_wavelength.csv'

    BPW21R.add_char_from_csv(pd_sensibility)
    MH_100.add_char_from_csv(ls_sensibility)

    pd_sensibility_area = BPW21R.integrate_char('relative_sensitivity_x_wavelength')
    ls_sensibility_area = MH_100.integrate_char('relative_output_x_wavelength')

    print(pd_sensibility_area)
    print(ls_sensibility_area)


if __name__ == '__main__':
    main()

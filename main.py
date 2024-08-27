"""Module to estimate Photodiode currente based on the Photodiode and Light source caracteristics"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from photodiode_model.light_source import LightSource
from photodiode_model.photodetector import Photodiode
import photodiode_model.char_math as CHAR_MATH

root_path = Path(__file__).parent

BPW21R = Photodiode(efective_area=7.5, reverse_voltage=0, sensitivity=9)
MH_100 = LightSource(power=100, luminous_flux=3000)


def main():
    """Main function."""
    # Photodiode = pd and light source = ls

    pd_sensibility = root_path/'data'/'photodetector_curves'/'relative_sensitivity_x_wavelength.csv'
    ls_sensibility = root_path /'data'/'light_source_curves'/'relative_output_x_wavelength.csv'

    BPW21R.add_char_from_csv(pd_sensibility)
    MH_100.add_char_from_csv(ls_sensibility)

    _, pd_x, pd_y = BPW21R.get_char('relative_sensitivity_x_wavelength')
    _, ls_x, ls_y = MH_100.get_char('relative_output_x_wavelength')

    pd_curve = [pd_x, pd_y]
    ls_curve = [ls_x, ls_y]

    limits = CHAR_MATH.common_limits(pd_x, ls_x)
    dx = 0.1
    new_pd_curve, new_ls_curve = CHAR_MATH.equally_sized_curves(pd_curve, ls_curve, dx, limits)

    new_pd_x = new_pd_curve[0]
    new_pd_y = new_pd_curve[1]

    new_ls_x = new_ls_curve[0]
    new_ls_y = new_ls_curve[1]

    _, ax1 = plt.subplots()
    ax1.scatter(pd_x, pd_y)
    ax1.scatter(ls_x, ls_y)
    # ax1.set_xticks(np.arange(-2, 13, 0.1), minor=True)
    ax1.set_title('Sensitivity X Wavelenght')
    ax1.set_xlabel('Wavelenght [nm]')
    ax1.set_ylabel('Relative Sensitivity')
    ax1.grid()

    _, ax2 = plt.subplots()
    ax2.scatter(new_pd_x, new_pd_y)
    ax2.scatter(new_ls_x, new_ls_y)
    # ax2.set_xticks(np.arange(-2, 23, 0.2), minor=True)
    ax2.set_title('Sensitivity X Wavelenght')
    ax2.set_xlabel('Wavelenght [nm]')
    ax2.set_ylabel('Relative Output')
    ax2.grid()

    plt.show()

    # Sensibility area of Light Source
    ls_sensibility_area = MH_100.integrate_char('relative_output_x_wavelength')
    print(f'{ls_sensibility_area} nm')
    # Luminous density
    ls_luminous_density = MH_100.luminous_flux / ls_sensibility_area # [lm/nm]
    # Spectral Transfer
    pd_sensibility_char = BPW21R.get_char('relative_sensitivity_x_wavelength')
    ls_output_char = MH_100.get_char('relative_output_x_wavelength')
    relative_transfer = CHAR_MATH.multiply(pd_sensibility_char, ls_output_char, dx)
    _, ax2 = plt.subplots()
    ax2.plot(relative_transfer[0], relative_transfer[1])
    # ax2.set_xticks(np.arange(-2, 23, 0.2), minor=True)
    ax2.set_title('Sensitivity X Wavelenght')
    ax2.set_xlabel('Wavelenght [nm]')
    ax2.set_ylabel('Relative Sensitivity')
    ax2.grid()
    plt.show()
    # Spectral Transfer Area
    transfer_area = np.trapezoid(x=relative_transfer[0], y=relative_transfer[1], dx=dx)
    # Luminous flux transferred
    luminous_flux_transferred = ls_luminous_density*transfer_area
    print(f'{luminous_flux_transferred} lm')
    # Illuminance Received by the Photo Diode
    illuminance_received = luminous_flux_transferred/(BPW21R.efective_area*1e-6)
    print(f'{illuminance_received} lx')
    # Estimated currente
    equivalent_current = BPW21R.sensitivity*illuminance_received
    print(f'{equivalent_current*1e-6} mA')


if __name__ == '__main__':
    main()

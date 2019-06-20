"""plot_utils module for plotting SEDs."""
# TODO: Add a log file
from __future__ import division, print_function

import matplotlib.pyplot as plt
import matplotlib
import scipy as sp
import matplotlib.ticker as ticker
from phot_utils import *


def extract_info(mags_dict):
    flux = []
    wave = []
    bandpass = []
    bands = []

    for band in mags.keys():
        # Get central wavelength
        leff = get_effective_wavelength(band)
        # Extract mag and error from dictionary
        mag = mags[band][0]
        mag_err = mags[band][1]
        # get flux, flux error and bandpass
        flx, flx_err = mag_to_flux(mag, mag_err, band)
        bp_l, bp_u = get_bandpass(band)
        bands.append(band)
        flux.append([flx * leff, flx_err * leff])
        wave.append(leff)
        bandpass.append([leff - bp_l, bp_u - leff])

        # print('Flux in band', end=' ')
        # print(band, end=': ')
        # print(flx, end=' ')
        # print(r'erg/cm2/s/um', end='; ')
        # print('Central wavelength:', end=' ')
        # print('{:2.3f}'.format(leff), end=' ')
        # print('Bandpass:', end=' ')
        # print('{:2.3f}'.format(bp_u - bp_l))

    wave = sp.array(wave_flux)
    flux = sp.array(flux)
    bandpass = sp.array(bandpass)
    bands = sp.array(bands)

    return wave, flux, bandpass, bands


def plot_SED(wave, flux, bandpass):

    # TODO: Finish the function

    ymin, ymax = flux[:, 0].min(), flux[:, 0].max()

    f, ax = plt.subplots()

    ax.scatter(wave, flux[:, 0], edgecolors='k', c='cyan', s=50, alpha=.85,
               linewidths=.5)
    ax.errorbar(wave, flux[:, 0], xerr=bandpass, yerr=flux[:, 1], fmt='o',
                ecolor='k', color='turquoise', marker=None, alpha=.6)
    ax.set_ylim([ymin * .8, ymax * 1.1])
    ax.set_xscale('log', nonposx='clip')
    ax.set_yscale('log', nonposy='clip')
    ax.set_xlabel(r'$\lambda (\mu m)$')
    ax.set_ylabel(r'$\lambda$F (erg cm$^{-2}$s$^{-1}$)')
    ax.set_xticks(range(1, 11))
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())

    pass
#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit


def gaus(x, A, mu, sigma):
    return A * numpy.exp(-(x - mu)**2/(2 * sigma**2))


def fitter(x, A0, mu0, sig0, A1, mu1, sig1):
    return gaus(x, A0, mu0, sig0) + gaus(x, A1, mu1, sig1)


bins, counts = numpy.loadtxt('two_peaks.txt', unpack=True)
pars, _ = curve_fit(fitter, bins, counts)
print(pars)

x = numpy.linspace(bins[0], bins[-1], 100)
plt.scatter(bins, counts)
plt.plot(x, fitter(x, *pars))
plt.plot(x, gaus(x, *(pars[:3])))
plt.plot(x, gaus(x, *(pars[3:])))
plt.show()


#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy
from scipy.optimize import curve_fit


time, decays = numpy.loadtxt('decay.txt', unpack=True, delimiter=',')
print(time)
print(decays)

plt.plot(time, decays, 'ko')
plt.semilogy()
plt.show()

def f(t, l, n0):
    return n0 * numpy.exp(-l * t)

pars, _ = curve_fit(f, time, decays)
print(pars)

plt.plot(time, decays, 'ko')
plt.plot(time, f(time, *pars), 'r-')
plt.semilogy()
plt.show()


#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy


bins, counts = numpy.loadtxt('sunspots.txt', unpack=True)

fig, ax = plt.subplots(1, 1)
ax.plot(bins[:250], counts[:250], linestyle='steps-mid')
fig.savefig('sunspots.png')
plt.show()


#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy


bins, counts = numpy.loadtxt('sunspots.txt', unpack=True)

# let's find our running averages using arrays
data = numpy.vstack((counts[:-4], counts[1:-3], counts[2:-2],
                     counts[3:-1], counts[4:]))
average = data.mean(axis=0)
# the above works for our 5-bin window, or we can create the list
window = 5
data_to_merge = []
for i in range(window):
    if i != window - 1:
        data_to_merge.append(counts[i:1 - window + i])
    else:
        data_to_merge.append(counts[i:])
# let's just check to make sure everything looks right
# running array.shape is similar to len(array), but if the array is
# multidimensional, we get all dimensions at the same time
for entry in data_to_merge:
    print(entry.shape)

data = numpy.vstack(data_to_merge)
# but we still need just our means...
average = data.mean(axis=0)

# we could also just add those array slices together
average = (counts[:-4] + counts[1:-3] + counts[2:-2] +
           counts[3:-1] + counts[4:]) / 5

plt.plot(bins, counts, linestyle='steps')
plt.plot(bins[2:-2], average, color='k')
plt.xlim([0, 132])  # only look at some of the data
plt.ylim([0, 160])
plt.show()

# if we wanted to save a plot, we can do this:
fig, ax = plt.subplots(1, 1)
ax.plot(bins[:250], counts[:250], linestyle='steps')
fig.savefig('sunspots.png')
plt.show()


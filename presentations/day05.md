# numpy and matplotlib

Mike Moran

`mmoran9@nd.edu`

21 June 2016

!

## Convention

```
import matplotlib.pyplot as plt
import numpy
```

...or...

```
import numpy as np
```

!

## Create an array

All of these create the same array:

```
a = numpy.array([0, 1, 2])
b = numpy.arange(3)
c = numpy.linspace(0, 2, 3)
```

!

## Math with arrays

Basic math: `a + b`, `numpy.sqrt(a)`

Basic stats: `a.mean()`, `a.std()`

- for multidimensional arrays, specify an axis if necessary: `a.mean(axis=0)`

Linalg: `a.dot(b)`, `numpy.cross(a, b)`

!

## Random points

```
from random import random
points = [[random(), random()]
          for _ in range(100)]

points = numpy.random.rand(100, 2)
```

How would you separate these out into *x* and *y* arrays?

!

## Let's plot!

```
plt.plot(x, y)
plt.show()
```

Need help? [http://matplotlib.org/api/pyplot_api.html](http://matplotlib.org/api/pyplot_api.html)

!

## Sunspots

Total observed number of sunspots for each month starting in January, 1749 

- Read in `sunspots.txt`, and plot it

- Change the plot to *not* be a connected line graph

- On the same plot, include a moving average (window = 5)

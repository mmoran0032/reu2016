# Special Topics in Standard Python

Mike Moran

`mmoran9@nd.edu`

16 June 2016

!

## Special collections

Aside from lists, tuples, sets, and dictionaries, there are a few special-case
collections we can use

```
import collections

counter = collections.Counter()
colors = ['red', 'blue', 'red',
          'green', 'blue', 'blue']
for word in colors:
    counter[word] += 1

Isotope = collections.namedtuple(
    'Isotope', ['symbol', 'A', 'Z'])
he4 = Isotope('He4', 4, 2)
```

!

## Testing

`assert condition is True`

- stops program execution if condition is false

- useful for making sure we read in the right amount of data, for instance

!

## Lists expanded

Create a string from a list: `''.join(l)`

- everything in `l` must be a string

Quickly create a list from a sequence:

- `l = [i**2 for i in range(10)]`

- Great for file processing!

!

## Lists for math

- If a list contains *only* numbers, we can treat it as a vector:
  
  `v = [0., 0., -9.81]`

- If a nested list contains *only* numbers, we can treat it as a matrix:
  
  `m = [[0, 1], [1, 1]]`

- This is inefficient, but we don't know a better way yet...

!

## Special for-looping functions

We already know about `range`

`enumerate` gets the value and index

`zip` "walks" through two lists at the same time

!

## Protecting yourself

We place operations within these blocks to safeguard ourselves from unwanted
operations (bad division, importing the wrong thing, requiring user input, etc.)

```
try:
    x = 5 / 0
except:
    print('divided by zero')
    x = 0.
```

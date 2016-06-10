# Looping and File Processing

Mike Moran

14 June 2016

!

## From last time...

!

## `while`

Basic structure:

```
while condition is True:
    do_something()
    update_condition()
```

- condition can be anything that returns a *boolean* (usually math-related)

- without update, infinite loop

!

## `for`

Basic structure:

```
for item in container:
    do_something_with(item)
```

- container is an *iterable* (list, tuple, string, sequence, or *generator*)

- if you just want numbers, use `range`

!

## Estimating π

Srinivasa Ramanujan discovered an infinite series for π:

![](./Images/pi.png)

!

## Basic file reading

```
f = open(filename, 'r')
f.read()
f.close()
```

!

## Better file reading

```
with open(filename, 'r') as f:
    f.read()
```

!

## "Best" file reading

```
import csv

with open(filename, 'r') as f:
    # using default delimiter
    reader = csv.reader(f, delimiter=',')
    next(reader)
```

!

## Get everything

loop over the file:
```
for line in file:
    # save line
for line in reader
    # save line
```

...and python has a trick for this...

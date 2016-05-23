# Special Topics in Standard Python

Mike Moran

16 June 2016

!

## What's left?

More with strings

Using builtin structures for mathematics

Avoiding the program exiting early

!

## Strings as 'lists'

`s[a:b]` works the same as `l[a:b]`

Create a string from a list: `''.join(l)`

- everything in `l` must be a string

!

## Even better file processing!

```
data = [line for line in f]
```

Avoids creating/appending to a list, and is *much* faster!

So, knowing this, let's change our work from last time...

!

## How do we know?

Timing (profiling) is essential for complex algorithms

```
import datetime

start = datetime.datetime.now()
# code to time
stop = datetime.datetime.now()
total_time = stop - start
```

!

## Lists for math

- If a list contains *only* numbers, we can treat it as a vector:
  
  `v = [0., 0., -9.81]`

- If a nested list contains *only* numbers, we can treat it as a matrix:
  
  `m = [[0, 1], [1, 1]]`

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

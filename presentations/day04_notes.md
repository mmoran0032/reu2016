04: Special Topics in Standard Python
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We can use `for/while` loops to perform repeated actions or move through a
  data structure

- We can read data from a file, write to a file, and save the data in a
  structure to use later

- We won't be able to cover all of this in class, but I'm keeping all of the
  notes in here so that you have some additional guidance for your own study


Special collections
--------------------------------------------------------------------------------

- Python has more than just lists, tuples, sets, and dictionaries, available
  through the `collections` module

- `collections.Counter` provides an easy way to count up items within a list
  - Edit your code from Tuesday to count up the occurrences words in
    `northwind.txt`, and print out the 10 most common (`c.most_common(num)`)

- `collections.namedtuple` provides an easy way to create records

- Example code:
  ```python
  import collections

  counter = collections.Counter()
  colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
  for word in colors:
      counter[word] += 1

  Isotope = collections.namedtuple('Isotope', ['symbol', 'A', 'Z'])
  he4 = Isotope('He4', 4, 2)
  ```


Testing
--------------------------------------------------------------------------------

- I've shown you this before, but here it is again, since it is important to
  know how to test your code:
  ```python
  assert condition is True
  # following only runs if condition is met
  ```
  The `condition is True` can be anything, but usually is number comparison

- You can call functions within the statement, such as `assert len(l) == 5`

- We won't spend a lot of time on this, but know that a lot of times you'll want
  to test you code


Strings revisited
--------------------------------------------------------------------------------

- We can do almost all of the same things to strings as we can to lists

- Looping over a string is *identical* to looping over a list

- From last time, instead of just splitting the words up, let's get some
  statistics (most frequent word, letter frequency) from the data

- From last time, let's create a new file that contains the bin, counts, and
  uncertainty in the counts for the data
  - requires creating a string to write to the file

- We can also combine a list of strings into a single string, joined by whatever
  input string you use:
  ```python
  s = '\n'.join(l)  # puts newlines between items in the list
  s = ' in between '.join(l)
  ```
  - This is a nice way to create a string to write to a file

- String formatting: `'values: {}, {}'.format(value1, value2)`

  - You can include a whole lot more information in here

Lists and file processing revisited
--------------------------------------------------------------------------------

- We'll do this a bunch of times and save the numbers, so we have a basic set of
  data to help guide some analysis later on...

- Creating and appending to a list is *slow!*
  - Let's time how long it takes:
    ```python
    from datetime import datetime as dt

    start = dt.now()
    l = []
    for i in range(100000):
        l.append(i)
    end = dt.now()

    print((start - end).total_seconds())
    ```

    - How can we turn this into a function?

- Python has a better way, called *list comprehension*:
  ```python
  l = [i for i in range(100000)]
  ```
  - Try timing it with your function and compare

  - This is extremely useful for a lot of different situations, like file
    processing:
    ```python
    with open(filename, 'r') as f:
        data = [line.split() for line in f]
    ```

- Let's take that data file, and load it in using our list comprehension, then
  create two lists containing the individual data series


Lists as mathematical objects
--------------------------------------------------------------------------------

- A list is a decent stand-in for a vector, so let's try writing our own
  mathematical functions using lists.
  - Just create a dot and cross product
  - First, do this with what you know right now

- `enumerate` and `zip` are great! Let's talk about them...

- Can create a nested list (you've already encountered these before) to act as
  a matrix
  - How would you then do matrix multiplication?
  - **Example:** find the *nth* Fibonacci number using a matrix

`try/except`
--------------------------------------------------------------------------------

- These block protect against unwanted operations that would end your program

- We can safeguard ourselves without interrupting the program flow

- *Extremely* useful for making sure that our imports are working well
  ```python
  try:
      import numpy
      print('numpy: ', numpy.__version__)
  except ImportError:
      print('numpy not installed')
  ```

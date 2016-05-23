04: Special Topics in Standard Python
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We can use `for/while` loops to perform repeated actions or move through a
  data structure

- We can read data from a file, write to a file, and save the data in a
  structure to use later


Strings revisited
--------------------------------------------------------------------------------

- We can do almost all of the same things to strings as we can to lists

- Looping over a string is *identical* to looping over a list

- From last time, instead of just splitting the words up, let's get some
  statistics (most frequent word, letter frequency) from the data

- From last time, let's create a new file that contains the bin, counts, and
  uncertainty in the counts for the data
  - requires creating a string to write to the file


Lists and file processing revisited
--------------------------------------------------------------------------------

- Creating and appending to a list is *slow!*
  - Let's time how long it takes:
    ```python
    import datetime

    start = datetime.datetime.now()
    l = []
    for i in range(100000):
        l.append(i)
    end = datetime.datetime.now()

    print(start - end)
    ```

    - How can we turn this into a function?

- Python has a better way, called *list comprehension*:
  ```python
  l = [i for i in range(100000)]
  ```
  - Try timing it with your function and compare

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
      print(numpy.__version__)
  except ImportError:
      print('numpy not installed')
  ```

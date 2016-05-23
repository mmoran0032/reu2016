02: Functions and Containers
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We can define our own functions using the `def` statement

- Variables can be defined and used later, and even function can be saved as
  variables and used later (including being passed into other functions)


`bisection.py`
--------------------------------------------------------------------------------

- Finds the root of a function via the bisection method (range of potential
  roots cut in half at every iteration)

- Take a look at the code, run it, and figure out what everything does (add in
  comments if necessary)

- What happens when you change the tolerance? How can you use different
  functions within the code?


Container types
--------------------------------------------------------------------------------

- python uses four basic types of containers: lists, tuples, sets, and
  dictionaries
  - We'll mostly use lists and tuples during the course, but know that the
    others are helpful in different situations

- Lists hold a group of items (numbers) in a sequence, and can be edited to add
  or subtract items from the list, or adjust items within the list

- Tuples are lists, but can't be changed after you create them

- Talk more about lists, creation, editing, access
  - new list: `l = []` (empty)
  - add to the list: `l.append(value)`
  - find length of list: `len(l)`
  - get second value from list: `l[1]`
  - get slice of the list: `l[2:5]; l[:4]; l[-3:]`

- Update `bisection.py` to use lists where it makes sense

- Update `bisection.py` to make better use of functions


`if/elif/else`
--------------------------------------------------------------------------------

- Used to control flow by checking a condition or conditions
  ```python
  x = 5
  if x > 10:
      print('x is large')
  elif x > 2:
      print('x is medium')
  elif x >= 0:
      print('x is small')
  else:  # x < 0
      print('x is negative')
  ```

- You can nest if statements, and the blocks can be any number of lines long.

- You can call functions within the statements: `if len(l) > 4:`

- Check if item in something: `if 'x' in test_string:`

- When you're comparing items, you can use `in` to see if something is in a
  container, `isinstance` to see if a variable is something, and many others


Strings
--------------------------------------------------------------------------------

- Strings are everywhere in python, and we can convert them between different
  types easily:
  - `int(s), float(s)` to get numbers
  - `s.split()` to break the string up by whitespace (default) or whatever you
    pass into `split` and save them in a list

- They also have special processing to make things easier:
  - `s.strip()` removes leading and trailing whitespace

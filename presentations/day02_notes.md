02: Functions and Containers
================================================================================

Windows users
--------------------------------------------------------------------------------

- Look into the guide [here](https://www.davidbaumgold.com/tutorials/set-up-python-windows/)
  for using python on Windows with Cygwin. It is an alternative to using IDLE,
  and you will be learning bash at the same time. Your work would more closely
  follow what I do in class.


Refresher from last time
--------------------------------------------------------------------------------

- We can define our own functions using the `def` statement

- Variables can be defined and used later, and even function can be saved as
  variables and used later (including being passed into other functions)

- In fact, let's just look at some code to remind us how everything works!
  Download `stack_example.py` from the website and check it out.


`bisection.py`
--------------------------------------------------------------------------------

- Finds the root of a function via the bisection method (range of potential
  roots cut in half at every iteration)

- Take a look at the code, run it, and figure out what everything does (add in
  comments if necessary)

- What happens when you change the tolerance? How can you use different
  functions within the code?


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


Container types
--------------------------------------------------------------------------------

- python uses four basic types of containers: lists, tuples, sets, and
  dictionaries
  - We'll mostly use lists and tuples during the course, but know that the
    others are helpful in different situations

- Lists hold a group of items (numbers) in a sequence, and can be edited to add
  or subtract items from the list, or adjust items within the list

- Tuples are lists, but can't be changed after you create them

- Lists are zero-indexed, so the first item is accessed with `0`, the second
  item with `1`, etc. You can also count backwards, with `-1` being the last
  item, `-2` being the second-to-last, etc.

- Talk more about lists, creation, editing, access
  - new list: `l = []` (empty)
  - add to the list: `l.append(value)`
  - remove an item: `del l[2]`
  - combine lists: `l1 + l2 + l3; l1.extend(l2); l1 += l2`
  - find length of list: `len(l)`
  - get second value from list: `l[1]`
  - get slice of the list: `l[2:5]; l[:4]; l[-3:]; l[::2]`

- Update `bisection.py` to use lists where it makes sense

- Update `bisection.py` to make better use of functions


Better output
--------------------------------------------------------------------------------

- For large lists, just trying to print them usually looks bad, so we can use
  the `pprint` module:
  ```python
  from pprint import pprint

  # create large list here...
  pprint(l)
  ```

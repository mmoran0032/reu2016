01: Introduction to Python
================================================================================

Welcome
--------------------------------------------------------------------------------

- I've been using python for almost a decade, and have been teaching it to
  people for roughly half that time

- Work in experimental nuclear astrophysics, so class will be slightly tilted
  toward how I use python

- Will start with a foundation and add in concepts as we go, so important to
  keep up and ask questions

- We'll use live coding interspersed with you doing individual and pair coding

- Worksheets will guide the class, but aren't turned in and are for your own
  benefit

- Notes/presentations are written in Markdown (easy formatting in plain text)


Who are you?
--------------------------------------------------------------------------------

- Gauge current programming experience, then talk about different ways that they
  may have actually programmed before

- Experimental vs. theory (this course is geared toward both, but with an
  applied focus)


Getting help
--------------------------------------------------------------------------------

- Google/stackoverflow are your friend! Searching `python3 [thing to search]` is
  completely fine!

- Python documentation is very helpful: https://docs.python.org/3/


Basic math operations
--------------------------------------------------------------------------------

- `+ - * / // %`: what do these mean? Try them out!

- `import math; math.cos(math.pi)` for more advanced functions

- Use `help(math)` to see everything, `help(math.cos)` for just that function

- If `h = 6.62606876e-34`, how can you calculate hbar?

- Which of these work on strings? (We'll talk more about this later...)


Functions, variables, and strings (Intro)
--------------------------------------------------------------------------------

- create a string: `'stuff'`
  - strings can have numbers: `'45' != 45`
  - strings with numbers don't act like numbers

- display stuff on the screen: `print('stuff')`

- save something to display later: `saved_string = 'stuff'`

- Size of a string: `len(saved_string) == 5`


Creating a program
--------------------------------------------------------------------------------

- Instead of typing in all of our code line by line, we can create a program

- Basic structure:
  ```python
  #!/usr/bin/env python3

  import math

  print(math.cos(math.pi))
  ```

- Now, we need to run it!


Defining your own functions
--------------------------------------------------------------------------------

- Basic structure:
  ```python
  def function_name(input_variable):
      # do something with input variable...
      value = input_variable
      return value
  ```

- You can't use the same name as a builtin function (so don't)


Comments and docstrings
--------------------------------------------------------------------------------

- Comments can be placed anywhere, but everything on the line after them is
  treated as a comment

- Denoted by `# comment`
  - Convention: if an inline comment, two spaces before the comment starts

- Docstrings are "super comments" for functions and the program itself
  ```python
  #!/usr/bin/env python3

  ''' test.py - testing program
      looks at how comments are structured
  '''

  def square_it(number):
      '''returns the square of the number'''
      return number**2
  ```

- Helpful for documentation, and should be used where the code may be confusing
  or to remind yourself of what you did later.


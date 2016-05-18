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


Who are you?
--------------------------------------------------------------------------------

- Gauge current programming experience, then talk about different ways that they
  may have actually programmed before

- Experimental vs. theory (this course is geared toward both, but with an
  applied focus)


Functions, variables, and strings (Intro)
--------------------------------------------------------------------------------

- create a string: `'stuff'`
  - strings can have numbers: `'45' != 45`
  - strings with numbers don't act like numbers

- display stuff on the screen: `print('stuff')`

- save something to display later: `stuff = 'stuff'`


Basic math operations
--------------------------------------------------------------------------------

- `+ - * / // %`: what do these mean? Try them out!

- `import math; math.cos(math.pi)` for more advanced functions

- Use `help(math)` to see everything, `help(math.cos)` for just that function

- If `h = 6.62606876e-34`, how can you calculate hbar?


Creating a program
--------------------------------------------------------------------------------

- Instead of typing in all of our code line by line, we can create a program

- Basic structure:
  ```python
  #!/usr/bin/env python3

  import math

  print(math.cos(math.pi))
  ```

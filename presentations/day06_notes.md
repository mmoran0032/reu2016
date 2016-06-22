06: Numerical Methods
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We can create an use arrays for easier numerical processing and mathematics,
  and those arrays can be read in from a file quickly and easily

- We can plot results using `matplotlib` and control the look of those plots

- We'll do a long refresher over this, including the full solution for the
  moving average, at the start of class


Overview
--------------------------------------------------------------------------------

- Since we can't cover the full range of possible topics, we'll focus on two

- There is a lot more to this than just what we'll learn about here, and many
  more regions of numerical physics that you might encounter, so explore things
  on your own as well!


Integration
--------------------------------------------------------------------------------

- If they ask, give the example about reaction rate calculations that almost
  have to be done numerically

- Easiest way to integrate is the trapezoid method, so let's write this as a
  basis for our integration. We know we can do better, but for now, this is
  a good start

- We'll implement Simpson's method, specifically the Simpson's 3/8ths rule:
  ```python
  h = (b - a) / 3
  factor = f(a) + 3*f((2*a + b) / 3) + 3*f((a + 2*b) / 3) + f(b)
  integral = (3 * h / 8) * factor
  ```

- This is just the default form, and we can extend it to have an arbitrary
  number of intervals relatively easily
  ```python
  h = (b - a) / n
  xi = a + i*h
  3*h/8 * (f(x0) + 3f(x1) + 3f(x2) + 2f(x3) + 3f(x4) + ... + f(xn))
  ```
  This only works if `n` is a multiple of 3



Root Finding
--------------------------------------------------------------------------------

- We've done bisection before, but it is slow and inefficient

- We can use two similar iterative methods to find roots much more quickly

- Newton's method:
  - We need the function and its first derivative defined
  - We need one starting points
  - Iterative process:
    ```
    x1 = x0 - f(x0)/f'(x0)
    ```

- Secant method:
  - We only need the function defined
  - We need two starting points
  - Iterative process:
    ```
    x2 = x1 - f(x1) * (x1 - x0)/(f(x1) - f(x0))
    ```

- For both, we need to make sure we have an idea about convergence, and to avoid
  division by zero errors

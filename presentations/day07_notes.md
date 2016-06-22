07: Numerical Methods with SciPy
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We implemented a couple of algorithms by hand to understand what was going on
  for each of them, and to learn a little more about using NumPy

- This was a lot of work, and is prone to errors, and usually runs slower than
  an already implemented version of the routine


Overview
--------------------------------------------------------------------------------

- SciPy's module structure feels like we're going through a directory structure
  - You'll see similar things with complex packages, and we've already
    encountered one example of this (`numpy.random`)

- We'll being using the `from something import something_else` import statement
  most of the time

- We'll also cover things that we couldn't easily implement ourselves, like
  linear algebra and curve fitting

- Again, there is still a lot more to this than what we'll cover, so explore the
  documentation to discover what else there might be


What we did last time
--------------------------------------------------------------------------------

- Integration methods are in `scipy.integrate`:
  - [Documentation](http://docs.scipy.org/doc/scipy/reference/integrate.html)

  - You'll also see that the same package is used for ODE solving, which is just
    a different form of integration

  - There is a difference between having a functional form that you're
    integrating and a sequence of points, so make sure that you check what the
    function signature (what you need to pass into the function) is

  - Simpson's method and the trapezoid method take sequences, not functions

- Root finding methods are in `scipy.optimize`:
  - [Documentation](http://docs.scipy.org/doc/scipy/reference/optimize.html)

  - This is a **large** package, with a ton of stuff in it!

  - Specifically, we want root finding methods for scalar functions, aptly
    named `bisect` and `newton`
    - `newton(f, x0, fprime=None)` defaults to the secant method if we don't
      provide a functional form of the derivative


Curve Fitting
--------------------------------------------------------------------------------

- Almost any experimental analysis includes some form of curve fitting, so let's
  learn how to do this

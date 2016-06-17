# Numerical Methods

Mike Moran

`mmoran9@nd.edu`

23 June 2016

!

## Main Topics

1. Integration

1. Linear Algebra

1. Root Finding

1. Differential Equations

1. Others...?

Explore these on your own too, since we won't be able to cover everything...

!

## Main Topics

1. **Integration**

1. Linear Algebra

1. **Root Finding** (we've done this before)

1. Differential Equations

1. Others...?

Explore these on your own too, since we won't be able to cover everything...

!

## Integration

!

We'll just focus on implementing Simpson's 3/8 rule:
```
h = (b - a) / 3
factor = (f(a) +
          3*f((2*a + b) / 3) +
          3*f((a + 2*b) / 3) +
          f(b))
integral = (3 * h / 8) * factor
```

!

## Root Finding

!

## But why?

Bisection method is slow and inefficient, and we can do better

Alternatives:

- Newton's method (if we know the functional form of the derivative)

```
x1 = x0 - f(x0)/f'(x0)
```

- Secant method (if we don't)

```
x2 = x1 - f(x1) * 
     (x1 - x0)/(f(x1) - f(x0))
```

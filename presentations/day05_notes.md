05: Introduction to NumPy and Matplotlib
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- Using lists as mathematical objects is not good! We had to use a bunch of code
  for basic operations, and didn't have a lot of functionality

- There are ways to optimize code to run faster in basic python, especially when
  dealing with saving data in a container and reading from files


Creating arrays and basic math
--------------------------------------------------------------------------------

- Basic array is created with `numpy.array([0, 1, 2])` unless created directly
  with a special function

- Arrays work differently than lists when talking about math and slices
  - transposition `a.T`, dot products `a.dot(b)`, statistics `a.mean()`
  - fancy slices for matrix-like objects `a[:, 1]`

- Basic math operations are also included, but act on each element separately

- If you need random points, you should use `numpy.random.rand(r, c)`


Plotting
--------------------------------------------------------------------------------

- At the most basic level, `plt.plot(x, y)` will create a connected line graph

- You can pass additional options to plot to change the graph type

- Histograms are made differently, and take in an array that then generates the
  resulting histogram: `plt.hist(data, bins=5)`

- Everything can be controlled, so look at the documentation

- To display, you need to run `plt.show()`, and program execution waits


Read in data
--------------------------------------------------------------------------------

- We can use our regular python version, or use `numpy.loadtxt`

- If you have multiple columns of data, you can immediately create two arrays
  with `numpy.loadtxt(filename, unpack=True)`

- Again, look at the reference pages to see all of the options available


Sunspot data
--------------------------------------------------------------------------------

- Data contains the total sunspots for each month

- Moving average is given by:
  - `Y_k = \frac{1}{2r}\sum_{m=-r}^r y_{k+m}`
  - `r = 5` is pretty good, and `y_k` are the individual sunspot numbers

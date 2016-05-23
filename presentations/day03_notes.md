03: File Processing
================================================================================

Refresher from last time
--------------------------------------------------------------------------------

- We can control flow within the program with `if/elif/else` blocks

- Lists are a good way to store basic data


`for/while` Loops
--------------------------------------------------------------------------------

- Think of for being for each, so for each item in a container
  ```python
  for item in user_list:
      print('user: {}'.format(item))
  ```
- Looping is commonly done over items within a list/string, or just an index
  number (using `range([start,] stop[, step]`)

- A nice additional thing, if you want the index *and* the item, is to use
  `enumerate`: `for i, value in enumerate(user_list)`

- While loops work similarly to if statements, but will continue performing
  actions until some condition is met
  - You need to make sure that you update whatever variable is needed for the
    condition within the loop, otherwise the loop will never finish


Example: Srinivasa Ramanujan
--------------------------------------------------------------------------------

- Way to estimate π:

  ![](./pi.png)

- What else do we need to program in order to figure this out?


File processing
--------------------------------------------------------------------------------

- Most scientific work involves reading from and writing to files to store or
  access data
  - Python is great with this, since it works very well with strings and files
    without much "boilerplate" code

- Use basic UNIX path conventions to access files (`.` is current directory,
  `..` is the directory above, `/` to separate directories)

- Basic structure (reading):
  ```python
  f = open(filename, 'r')
  f.read()  # f.readline() for just one line
  f.close()
  ```
  - `read/readline` return an empty string if they have reached the end of the
    file, so you can use this as a "sentinel" value
  - An empty line still contains a newline (`\n`) character

- Basic structure (writing):
  ```python
  f = open(filename, 'w')
  f.write('string to write\n')
  f.close()
  ```


Saving data from files
--------------------------------------------------------------------------------

- Loop over the data or read until you have everything you need (`for` loops are
  great to use here!)

- In general, need to create an empty list, then append to it to save the data
  ```python
  data = []
  for line in f:
      # process line if necessary
      data.append(line)
  ```

- Python has a better way, called *list comprehension*:
  ```python
  data = [line for line in f]
  ```
  - We can post-process this after forming the list, or using the `csv` module
    we already have some processing done


Example files
--------------------------------------------------------------------------------

- `nothwind.txt` separate by word to get used to file I/O

- `156dy_jul00_singles.txt` separate out into bin and counts as individual lists
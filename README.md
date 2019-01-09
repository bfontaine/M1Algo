# M1Algo

This is a school project for the [Algorithms class][algo] at Paris Diderot
University.

[algo]: http://www.liafa.univ-paris-diderot.fr/~francoisl/m1algo.html

## Usage

You’ll need Python ≥3.1.

```
./src/wrapper [-w <width>] --algo <algo> < input > output
```

The program reads one line on stdin and writes on stdout.

- `--algo <algo>`: specifies the algorithm to use (you *must* provide this
  information)
- `-w <width>`: specifies the width of the page (default: 79)
- `--info <algo>`: this option can be used to print some info about a specific
  algorithm
- `--justify`: justify the text
- `--ls`: list the available algorithms

Use `--help` to get a summary of the available options.

## Add an algorithm

Algorithms are defined as functions in files in `src/algos/`. To add a new
algorithm, open an existing file or create a new one in `src/algos/`. If this is
a new file, add the following lines at the top of it:

```python
# -*- coding: UTF-8 -*-
from .base import algo
```

Then, any algorithm must be a function with two parameters, the words list and
the width, and yields lines to print. This function must also be decorated with
`@algo()`, which takes an optional short doc which will show up when one uses
`--info` on the command line. The name of the function must be unique across
all `src/algos/*` files. You can define helper functions in the same file, as
long as you don’t use `@algo()` on them.

### Example

```python
@algo("return an empty text")
def empty(words, width):
    """
    This really cool algorithm has a complexity of O(1).
    """
    yield "no text here"
```

Please note that `words` may be a generator instead of a list.

## Tests

Run `make check`. If you have [coverage.py][cov] for Python3, you can check the
code coverage using `make covercheck`.

[cov]: http://nedbatchelder.com/code/coverage/

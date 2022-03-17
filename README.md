# Quick Start

Our project has no external dependencies; Python 3.6 or later should be sufficient.

Everything of interest to a researcher is exported from `Code/supernumber.py`. The following commands should be sufficient to start experimenting:

```
$ cd Code
$ python3
>>> from supernumber import SuperNumber, SuperNumbers
>>> import supernumber as sn
>>> from supernumber import SuperNumber
```

# Some examples

Creating a supernumber:

```
>>> SuperNumber(2, 5, 1)
<2 mod 5 | 1>
```

Multiplying supernumbers:

```
>>> x = SuperNumber(5, 9, 3)
>>> y = SuperNumber(7, 9, 3)
>>> x * y
<0 mod 9 | 3>
```

Checking equality of supernumbers:

```
>>> z = SuperNumber(7, 9, 3)
>>> z == y
True
```

Iterating over a set of supernumbers:

```
>>> [x for x in SuperNumbers(3, 1)]
[<0 mod 3 | 1>, <1 mod 3 | 1>, <2 mod 3 | 1>]
```

Testing some properties:

```
>>> sn.IsCommutativeSuperNumberMultiplication(1, 3)
True

>>> sn.HasSuperNumberIdempotentProperty(5, 1)
False

>>> sn.IsAssociativeSuperNumberMultiplication(7, 2)
True

>>> sn.SuperRootsOfOne(2,1)
[<1 mod 2 | 1>]


>>> x = SuperNumber(0,2,1)
>>> y = SuperNumer(1,2,1)
>>> sn.SuperNumberSetSpan({x,y})
{<1 mod 2 | 1>, <0 mod 2 | 1>}
```

# Running unit tests

Unit tests can be run as follows:

```
$ python3 Code/UnitTests.py
```

# Report

The report is formatted as a Jupyter notebook. If you have Jupyter installed (`$ pip3 install --user jupyter`), you can view an interactive version with this command:

```
$ jupyter-notebook Report.ipynb
```

There's also a PDF version.

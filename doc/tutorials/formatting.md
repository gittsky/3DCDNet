<!--
Created: Fri Nov 24 2023 14:26:53 GMT+0100 (Mitteleuropäische Normalzeit)
Modified: Mon Nov 27 2023 09:33:38 GMT+0100 (Mitteleuropäische Normalzeit)
-->

# Python code formatter and typing

This tutorial provides a guide on how to select the Black code formatter and typing to support type hints.

## Python code formatter

There are multiple python code formatter, but the most used one is `Black` .[^1] [^2]

### Installation

1. Install it with help of pip first:
    - `pip install black`
2. This package can now format single files, when entering following in the command line:

```console
black **/*.py
```

### Configuration for VSCode

1. Open the settings UI of VSCode by performing following:
    - Press `Ctrl + Shift + P` to open the Visual Studio Code Command Palette.
    - Search for `Preferences: Open User Settings` and press `Enter`.
    - Search for `black` in the settings and perform these operations:
        - Select `Black Formatter` in the `Editor: Default Formatter` section.
2. To enable the formatter to be activated when saving, search in the `Seetings` for `format on save mode`.
    - Check the checkbox under the section `Editor: Format On Save`.
    - Select `file` in the dropdown-menu under section `Editor: Format On Save Mode`, so the editor will format the whole file each time you save.

#### Example

1. For testing the installation and configuration, open an empty python-file in VSCode and write following code piece:

```python
# Imports 
## Numpy
import numpy as np
## Numpy data types
from numpy.typing import NDArray

## Python own data types
from typing import Callable

# Exception
class InvalidFooValue(Exception):
    "Raise if foo argument has the wrong value."
    pass 

def foobar(foo: int, bar: None | int | NDArray[np.int16] = None, baz: None | Callable[[int, int], int] = lambda x,y: x+y) -> list[int]:
    """Processes the input parameters and showcases docstrings and typing.

    The processing is based on the possible data types of the input parameters. Different arithmetic operations are performed depending on them.

    Parameters
    ----------
    foo : int
        Containing a integer value.
    bar : None | int | NDArray[np.int16] (N, 3), optional
        Containing None, int or a numpy array with shape (N, 3), by default None.
    baz : None | Callable[[int, int], int], optional
        If not None, it is a function , by default lambda x,y: x+y.

    Returns
    -------
    out : list[int]
        Processed data.

    Raises
    ------
    InvalidFooValue
        Raised if foo has a invalid value.

    See Also
    --------
    foobar2()
    
    Notes
    -----
    **Source:** this docstring style is based on this tutorial [1]_.
    **Notes for future coder:** it is optional, but supports conceptual documentation.
    
    References
    ----------
      [1] [Tutorial Docstrings](https://developer.lsst.io/python/numpydoc.html#py-docstring-short-summary)
      
    Examples
    --------
    A simple example for the usage of the function:

    >>> foobar(2)
    [ 2, 2 ]  
    """
    # Check for invalid foo values
    if foo == -1:
        raise InvalidFooValue()

    # Do some processing
    out = [-1]
    if bar is None:
        out = foo * [foo]
    else:
        if isinstance(bar, int):
            out = [baz(foo, bar) if baz is not None else foo * bar]
        else:
            out = bar.flat[0] * [foo]
            
    return out
```

2. Save the file and, if the installation worked, it should like this:

```python
# Imports
## Numpy
import numpy as np
## Numpy data types
from numpy.typing import NDArray

## Python own data types
from typing import Callable

# Exception
class InvalidFooValue(Exception):
    "Raise if foo argument has the wrong value."
    pass

def foobar(
    foo: int,
    bar: None | int | NDArray[np.int16] = None,
    baz: None | Callable[[int, int], int] = lambda x, y: x + y,
) -> list[int]:
    """Processes the input parameters and showcases docstrings and typing.

    The processing is based on the possible data types of the input parameters. Different arithmetic operations are performed depending on them.

    Parameters
    ----------
    foo : int
        Containing a integer value.
    bar : None | int | NDArray[np.int16] (N, 3), optional
        Containing None, int or a numpy array with shape (N, 3), by default None.
    baz : None | Callable[[int, int], int], optional
        If not None, it is a function , by default lambda x,y: x+y.

    Returns
    -------
    out : list[int]
        Processed data.

    Raises
    ------
    InvalidFooValue
        Raised if foo has a invalid value.

    See Also
    --------
    foobar2()

    Notes
    -----
    **Source:** this docstring style is based on this tutorial [1]_.
    **Notes for future coder:** it is optional, but supports conceptual documentation.

    References
    ----------
      [1] [Tutorial Docstrings](https://developer.lsst.io/python/numpydoc.html#py-docstring-short-summary)

    Examples
    --------
    A simple example for the usage of the function:

    >>> foobar(2)
    [ 2, 2 ]
    """
    # Check for invalid foo values
    if foo == -1:
        raise InvalidFooValue()

    # Do some processing
    out = [-1]
    if bar is None:
        out = foo * [foo]
    else:
        if isinstance(bar, int):
            out = [baz(foo, bar) if baz is not None else foo * bar]
        else:
            out = bar.flat[0] * [foo]

    return out
```

## Type checkers and linters

> 🚧 **UNDER CONSTRUCTION** 🚧

The Python runtime does not enforce function and variable type annotations, but it can help to minimize coding errors.[^3] To enforce the correct type annotations some python tools are of great help. For type checking it is suggested to use the `mypy` [^4] [^5] package, which is a static type checking tool.[^7]  
The core linters we will use will be an error and style linter. Error linters point out syntax errors or other code that will result in unhandled exceptions and crashes. On the other side style linters point out issues that don't cause bugs but make the code less readable or are not in line with style guides such as Python's PEP 8 document. `PyLint` provides both at the same time. [^6] [^8]

### Installtaion

### Setup

### Usage

## Typing

> 🚧 **UNDER CONSTRUCTION** 🚧

### Hints and best practises

[^1]: https://statusneo.com/introducing-black-the-uncompromising-python-code-formatter/ by Utkarsh Shukla, 24.11.2023
[^2]: https://github.com/life4/awesome-python-code-formatters by life4, 24.11.2023
[^3]: https://docs.python.org/3/library/typing.html by python, 24.11.2023
[^4]: https://github.com/python/mypy by mypy, 24.11.2023
[^5]: https://dev.to/jodaut/python-type-checking-with-visual-studio-code-46a7 by José David Ureña Torres, 24.11.2023
[^6]: https://inventwithpython.com/blog/2022/11/19/python-linter-comparison-2022-pylint-vs-pyflakes-vs-flake8-vs-autopep8-vs-bandit-vs-prospector-vs-pylama-vs-pyroma-vs-black-vs-mypy-vs-radon-vs-mccabe/ by  Al Sweigart, 24.11.2023
[^7]: https://makimo.com/blog/three-friends-of-the-better-code-style-python/ by Kamil Supera, 24.11.2023
[^8]: https://pypi.org/project/pylint/ by pylint, 24.11.2023
https://stackoverflow.com/questions/57220416/automatically-run-both-mypy-and-pylint-at-every-save

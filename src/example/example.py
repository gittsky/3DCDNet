#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   example.py
@Time    :   2023/11/14 16:52:51
@Author  :   Max Mustermann
@Version :   0.1
@Contact :   max.mustermann@ipm.fraunhofer.de
@License :   (C)Copyright 2023-2023, Fraunhofer-Institut für Physikalische Messtechnik IPM, Max Mustermann
@Desc    :   Example file to show the best practice of Python formating and linting.
@Source0 :   https://numpydoc.readthedocs.io/en/latest/format.html
@Source1 :   https://black.readthedocs.io/en/stable/
"""

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


class FooBarClass(object):
    """Example class.


    Here is a longer description of the use cases of this class.


    Attributes
    ----------
    foo : int
        Public class attribute containing a integer number.
    __bar : None | int | NDArray[np.int16] (N, 3), optional
        Private class attribute containing None, int or a numpy array with shape (N, 3), by default None.
    _baz : None | Callable[[int, int], int], optional
        Protected class attribute. If not None, it is a function, by default lambda x,y: x+y.

    Methods
    -------
    __call__(None) -> list[int]
        Double leading and tailing underscore method only if it has a special meaning defined by Python.
    __foobar(foo: int, bar: None | int | NDArray[np.int16] = None, baz: None | Callable[[int, int], int] = lambda x, y: x + y,) -> list[int]
        Private method triggered by the __call__().
    """

    def __init__(
        self,
        foo: int,
        bar: None | int | NDArray[np.int16] = None,
        baz: None | Callable[[int, int], int] = lambda x, y: x + y,
    ) -> None:
        """Constructor method.

        This function is not listed in the Methods section as it is the constructor method.

        Parameters
        ----------
        foo : int
            Containing a integer value.
        bar : None | int | NDArray[np.int16] (N, 3), optional
            Containing None, int or a numpy array with shape (N, 3), by default None.
        baz : None | Callable[[int, int], int], optional
            If not None, it is a function , by default lambda x,y: x+y.
        """

        self.foo = foo
        self.__bar = bar
        self._baz = baz

    def __foobar(
        self,
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

    def __call__(self) -> list[int]:
        """Callable instance method.

        This method will call the private __foobar method with the set class attributes.

        Returns
        -------
        list[int]
            Processed data.
        """
        return self.__foobar(self.foo, self.__bar, self._baz)

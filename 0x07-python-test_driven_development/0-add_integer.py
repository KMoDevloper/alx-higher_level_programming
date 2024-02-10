#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

:param a: The first integer.
:param b: The second integer (default is 98).
:return: The sum of a and b.
:raises TypeErroor: If a or b is not an integer or float.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The sum of a and b.
    :raises TypeError: If a or b is not an integer or float.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

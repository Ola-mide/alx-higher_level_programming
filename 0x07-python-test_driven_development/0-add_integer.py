#!/usr/bin/python3
"""
An addition module, an example below
>>> add_integer(2, 98)
100
"""


def add_integer(a, b=98):
    """
    A function that adds two integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result

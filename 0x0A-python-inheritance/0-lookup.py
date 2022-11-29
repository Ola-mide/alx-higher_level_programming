#!/usr/bin/python3
"""
A function that returns a list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    A function that returns a list of available attributes and methods
    of an object

    Args:
        obj (object): An object

    Returns:
        list: A list of available attributes and methods
    """
    return dir(obj)

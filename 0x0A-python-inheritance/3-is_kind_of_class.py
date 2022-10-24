#!/usr/bin/python3
"""
A function that checks if an object is an instance of a class
or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    or subclass

    Args:
        obj (object): The given object to be checked
        a_class (object): The specified class

    Returns:
        bool: True if obj is an instance of a_class or subclass or
        False if not
    """
    return isinstance(obj, a_class)

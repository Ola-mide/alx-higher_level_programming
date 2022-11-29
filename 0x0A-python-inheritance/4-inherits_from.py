#!/usr/bin/python3
"""
A function that checks if an object is an instance of a class
or subclass(directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    or subclass(directly or indirectly)

    Args:
        obj (object): The given object to be checked
        a_class (object): The specified class

    Returns:
        bool: True if obj is an instance of a_class or subclass(directly or
        indirectly) or False if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

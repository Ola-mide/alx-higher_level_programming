#!/usr/bin/python3
"""
A function that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    A function that checks if an object is an instance of a class

    Args:
        obj (object): The given object to be checked
        a_class (object): The specified class

    Returns:
        bool: True if obj is an instance of a_class or False if not
    """
    if type(obj) == a_class:
        return True
    else:
        return False

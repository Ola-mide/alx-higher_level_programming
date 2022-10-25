#!/usr/bin/python3
"""
A module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an
object
"""


def class_to_json(obj):
    """
    A module that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): an instance of a Class

    Returns:
        dict: dictionary representation for JSON serialization of an object
    """
    return obj.__dict__

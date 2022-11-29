#!/usr/bin/python3
"""
A module that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object

    Args:
        my_obj (object): The object whose JSON representation is to be gotten

    Returns:
        str: JSON representation of my_obj
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
"""
Module that returns an object representes by a JSON string
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object represented by a JSON string

    Args:
        my_str (str): A JSON string

    Returns:
        object: A data structure represented by the JSON string my_str
    """
    return json.loads(my_str)

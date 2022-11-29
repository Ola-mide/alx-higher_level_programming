#!/usr/bin/python3
"""
Module that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (object): Data structure whose JSON representation
        is written to a file
        filename (str): The name of the file where a JSON representation
        is written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

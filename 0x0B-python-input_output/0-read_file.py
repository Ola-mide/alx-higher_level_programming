#!/usr/bin/python3
"""
A module containing a function that reads a text file
"""


def read_file(filename=""):
    """
    A function that reads a text file

    Args:
        filename (str): The name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

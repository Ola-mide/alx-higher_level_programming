#!/usr/bin/python3
"""
A module that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file

    Args:
        filename (str): The name of the file that is appended to
        text (str): The string to be appended to the file

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

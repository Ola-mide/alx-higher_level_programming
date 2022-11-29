#!/usr/bin/python3
"""
A module that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file

    Args:
        filename (str): The name of the file to be written to
        text (str): The string written to the file

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

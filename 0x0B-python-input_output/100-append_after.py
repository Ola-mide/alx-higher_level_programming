#!/usr/bin/python3
"""
Module that inserts a line of text after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text after each line
    containing a specific string

    Args:
        filename (str): The name of the file
        search_string (str): The specific string to be located
        new_string (str): The line to be added if search_string is present
    """
    appended = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            appended += line
            if search_string in line:
                appended += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(appended)

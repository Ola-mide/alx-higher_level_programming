#!/usr/bin/python3
"""
A module that prints out a persons name
>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
    A function that says your name starting with 'My name is '
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

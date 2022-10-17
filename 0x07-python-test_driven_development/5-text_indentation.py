#!/usr/bin/python3
"""
A module that prints a text followed by a new line after specific characters
"""


def text_indentation(text):
    """
    A funtion that prints a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    length = len(text)
    idx = 0
    while idx < length:
        if text[idx] == ".":
            print(text[idx], end="")
            print("\n")
            idx += 1
            try:
                if text[idx] == " ":
                    idx += 1
                    pass
            except IndexError:
                pass
        elif text[idx] == "?":
            print(text[idx], end="")
            print("\n")
            idx += 1
            try:
                if text[idx] == " ":
                    idx += 1
                    pass
            except IndexError:
                pass
        elif text[idx] == ":":
            print(text[idx], end="")
            print("\n")
            idx += 1
            try:
                if text[idx] == " ":
                    idx += 1
                    pass
            except IndexError:
                pass
        else:
            print(text[idx], end="")
            idx += 1

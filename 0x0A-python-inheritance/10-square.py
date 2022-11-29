#!/usr/bin/python3
"""
A module containing the square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defining the Square class
    """
    def __init__(self, size):
        """
        Initializing an instance of the Square class

        Args:
            size (int): The height or width of the square
        """
        Rectangle.__init__(self, size, size)

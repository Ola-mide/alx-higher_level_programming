#!/usr/bin/python3
"""
Module for a square
"""


class Square:
    """
    Defining a square

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        The __init__ method initializes the object

        Args:
            size (int): The size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The area of the square
        
        Returns:
            The area of the square
        """
        return self.__size ** 2

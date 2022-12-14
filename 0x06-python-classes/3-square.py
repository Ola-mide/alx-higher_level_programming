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

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculating the area of the square

        Returns:
            integer: The area of the square

        """
        return self.__size ** 2

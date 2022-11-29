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
        self.size = size

    @property
    def size(self):
        """
        Retrieving the size value

        Returns:
            int: the size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setting the size value

        Args:
            value (int): the value set to size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculating the area of the square

        Returns:
            int: The area of the square

        """
        return self.__size ** 2

    def __eq__(self, square):
        """
        Implementing the comparator '=='

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() == square.area()

    def __ne__(self, square):
        """
        Implementing the comparator '!='

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() != square.area()

    def __gt__(self, square):
        """
        Implementing the comparator '>'

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() > square.area()

    def __ge__(self, square):
        """
        Implementing the comparator '>='

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() >= square.area()

    def __lt__(self, square):
        """
        Implementing the comparator '<'

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() < square.area()

    def __le__(self, square):
        """
        Implementing the comparator '<='

        Args:
            square (instance): an instance of the Square class

        Returns:
            bool: True or False

        """
        return self.area() <= square.area()

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
            integer: The area of the square

        """
        return self.__size ** 2

    def my_print(self):
        """
        Printing the square with a given size

        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("\n", end="")

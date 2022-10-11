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

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method initializes the object

        Args:
            size (int): The size of the square
            position (tuple): space to be left in x and y direction

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieving the size value

        Returns:
            int: the size of the square

        """
        return self.__size

    @property
    def position(self):
        """
        Retrieving the position tuple

        Returns:
            tuple: space to be left in x and y direction

        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setting the size value

        Args:
            value (int): the value set to size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        Setting the value of position

        Args:
            value (tuple): the value set to position

        Raises:
            TypeError: if value does not contain 2 positive integers

        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for a in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("\n", end="")

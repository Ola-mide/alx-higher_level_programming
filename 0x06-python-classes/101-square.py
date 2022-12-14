#!/usr/bin/python3
"""
Module for a square
"""


class Square:
    """
    Defining a square

    Attributes:
        size (int): The size of the square
        position (tuple): space to be left in x and y direction

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

    @property
    def position(self):
        """
        Retrieving the position tuple

        Returns:
            tuple: space to be left in x and y direction

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setting the value of position

        Args:
            value (tuple): the value set to position

        Raises:
            TypeError: if value is not a tuple containing two positive integer

        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculating the area of the square

        Returns:
            int: The area of the square

        """
        return self.__size ** 2

    def my_print(self):
        """
        Printing the square with a given size

        """
        if self.__size == 0:
            print("")
        else:
            print("\n"*self.__position[1], end="")
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print("\n", end="")

    def __str__(self):
        """
        Implementing the print() function into the Square class

        Returns:
            str: the specified square to be printed

        """
        stdout = ""
        if self.__size == 0:
            return stdout
        else:
            stdout += "\n"*self.__position[1]
            stdout += (" "*self.__position[0] + "#"*self.__size + "\n")\
                * (self.__size - 1)
            stdout += (" "*self.__position[0] + "#"*self.__size)
            return stdout

#!/usr/bin/python3
"""
A module that defines a rectangle class
"""


class Rectangle:
    """
    The rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        The __init__ function initailizes an instance of the Rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieving the width parameter

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting the width parameter

        Args:
            value (int): Value set to the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieving the height parameter

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting the height parameter

        Args:
            value (int): Value set to the height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

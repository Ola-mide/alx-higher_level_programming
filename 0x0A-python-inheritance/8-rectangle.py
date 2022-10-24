#!/usr/bin/python3
"""
A module containing a class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The rectangle class
    """
    def __init__(self, width, height):
        """
        Initializing an instance of the Rectangle class

        Args:
            width (int): The width
            height (int): The height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

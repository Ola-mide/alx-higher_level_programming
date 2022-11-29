#!/usr/bin/python3
"""
A module containing an class BaseGeometry
"""


class BaseGeometry(object):
    """
    A BaseGeometry class
    """
    def area(self):
        """
        A method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates its argument, value

        Args:
            name (str): name
            value (int): value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

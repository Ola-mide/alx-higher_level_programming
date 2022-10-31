#!/usr/bin/python3
"""Rectangle module"""
from models.base import *


class Rectangle(Base):
    """
    Defining the rectangle class

    Attr:
        width (int): width
        height (int): height
        x (int): x
        y (int): y
        id (int): id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieving width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width value

        Args:
            value (int): value set to width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height value

        Args:
            value (int): value set to height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieving x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting x value

        Args:
            value (int): value set to x

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieving y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting y value

        Args:
            value (int): value set to y

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculating the area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Displaying the rectangle using the '#' character"""
        for i in range(self.y):
            print("")
        for a in range(self.height):
            print(" " * self.x, end="")
            for b in range(self.width):
                print('#', end="")
            print("\n", end="")

    def __str__(self):
        """Overriding the __str__ method"""
        return "[{0}] ({1}) {2}/{3} - {4}/{5}".format(self.__class__.__name__,
                                                      self.id,
                                                      self.x,
                                                      self.y,
                                                      self.width,
                                                      self.height
                                                      )

    def update(self, *args, **kwargs):
        """Assigning new values to all attributes

        Args:
            args (list): no-keyword arguments
            kwargs (list): keyword arguments
        """
        attr = vars(self)
        attr_keys = list(vars(self).keys())
        idx = 0
        if len(args) != 0:
            for arg in args:
                attr[attr_keys[idx]] = arg
                idx += 1
        else:
            kwargs_keys = list(kwargs.keys())
            for key in kwargs_keys:
                if key == "id":
                    attr[key] = kwargs[key]
                else:
                    new = "_Rectangle__" + key
                    attr[new] = kwargs[key]

    def to_dictionary(self):
        """Generating dictionary representation of Rectangle"""
        rectangle_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rectangle_dict

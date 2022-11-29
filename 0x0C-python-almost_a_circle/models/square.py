#!/usr/bin/python3
"""Square module"""
from models.base import *
from models.rectangle import *


class Square(Rectangle):
    """
    Defining the Square class

    Attr:
        size (int): The width and height of the square
        x (int): x
        y (int): y
        id (int): id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        self.size = size
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Retrieving width value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting size value

        Args:
            value (int): value set to size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overriding the __str__ method"""
        return "[{0}] ({1}) {2}/{3} - {4}".format(self.__class__.__name__,
                                                  self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width
                                                  )

    def update(self, *args, **kwargs):
        """Assigning new values to all attributes

        Args:
            args (list): no-keyword arguments
            kwargs (list): keyword arguments
        """
        attr = vars(self)
        if len(args) != 0:
            no_kw_args = ['id', 'size', 'x', 'y']
            idx = 0
            for arg in args:
                if no_kw_args[idx] == 'id':
                    attr[no_kw_args[idx]] = arg
                elif no_kw_args[idx] == "size":
                    new = "_Rectangle__width"
                    attr[new] = arg
                else:
                    new = "_Rectangle__" + no_kw_args[idx]
                    attr[new] = arg
                idx += 1
        else:
            kwargs_keys = list(kwargs.keys())
            for key in kwargs_keys:
                if key == "id":
                    attr[key] = kwargs[key]
                elif key == "size":
                    attr["_Rectangle__width"] = kwargs[key]
                else:
                    new = "_Rectangle__" + key
                    attr[new] = kwargs[key]

    def to_dictionary(self):
        """Generating dictionary representation of Square"""
        square_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return square_dict

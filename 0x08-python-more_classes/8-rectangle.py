#!/usr/bin/python3
"""
A module that defines a rectangle class
"""


class Rectangle:
    """
    The rectangle class

    Attributes:
        number_of_instances (int): Number of instances created
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The __init__ function initailizes an instance of the Rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculating the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculating the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Printing the rectangle
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    rect += str(self.print_symbol)
                rect += "\n"
            return rect[:-1]

    def __repr__(self):
        """
        String representation of the rectangle
        """
        x = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return x

    def __del__(self):
        """
        Deleting an instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checking if two rectangle instances are equal or not

        Args:
            rect_1 (object): A Rectangle object
            rect_2 (object): A Rectangle object

        Raises:
            TypeError: rect_1 and rect_2 must be an instance of Rectangle

        Returns:
            object: the biggest rectangle based on the area
            of one of them if they are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

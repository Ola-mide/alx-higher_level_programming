#!/usr/bin/python3
"""
A module containing a class that inherits from int
"""


class MyInt(int):
    """
    Defining the MyInt class
    """
    def __eq__(self, num):
        """
        Changing the functionality of "=="

        Args:
            num (int): an integer
        """
        return self.__int__() != num.__int__()

    def __ne__(self, num):
        """
        Changing the functionality of "=="

        Args:
            num (int): an integer
        """
        return self.__int__() == num.__int__()

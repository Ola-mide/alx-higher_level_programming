#!/usr/bin/python3
"""
Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieving the dictionary representation of a Student instance
        """
        return self.__dict__

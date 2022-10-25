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

    def to_json(self, attrs=None):
        """
        Retrieving the dictionary representation of a Student instance

        Args:
            attrs (list): Attribute names
        """
        if attrs is not None:
            dct = {}
            for attribute in self.__dict__:
                if attribute in attrs:
                    dct[attribute] = self.__dict__[attribute]
            return dct
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replacing attributes of Student instance

        Args:
            json (dict): A dictionary
        """
        for key in list(json.keys()):
            setattr(self, key, json[key])

#!/usr/bin/python3
"""
A module containing a base class
"""
import json
import os


class Base:
    """
    Defining the Base class

    Attr:
        __nb_objects (int): None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Args:
            id (int): Just an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Generating the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Generating the JSON string rep of list_dictionaries to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    i = obj.to_dictionary()
                    list_dict.append(i)
                json_rep = Base.to_json_string(list_dict)
                f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """Generating a list of JSON string representation, json_string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating an instance with all attributes set"""
        dummy = cls(2, 4, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Converting file to instance"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            json_str = ""
            with open(filename, 'r', encoding="utf-8") as f:
                for x in f:
                    json_str += x
            json_list = cls.from_json_string(json_str)
            output = []
            for dictionary in json_list:
                instance = cls.create(**dictionary)
                output.append(instance)
            return output

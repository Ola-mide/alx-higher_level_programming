#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value == None:
        return a_dictionary
    else:
        new = a_dictionary.copy()
        keys = new.keys()
        for key in keys:
            if a_dictionary[key] == value:
                a_dictionary.pop(key, value)
        return a_dictionary

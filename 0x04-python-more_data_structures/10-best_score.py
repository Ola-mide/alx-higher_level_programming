#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        values = sorted(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == values[-1]:
                return key

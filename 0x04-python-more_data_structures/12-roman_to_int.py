#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    else:
        integer = 0
        roman_list = list(roman_string)
        length = len(roman_list) - 1
        roman_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        while length >= 0:
            integer += roman_dict[roman_list[length]]
            if length == 0:
                break
            elif roman_list[length] == 'M':
                if roman_list[length - 1] == 'C':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            elif roman_list[length] == 'D':
                if roman_list[length - 1] == 'C':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            elif roman_list[length] == 'C':
                if roman_list[length - 1] == 'X':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            elif roman_list[length] == 'L':
                if roman_list[length - 1] == 'X':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            elif roman_list[length] == 'X':
                if roman_list[length - 1] == 'I':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            elif roman_list[length] == 'V':
                if roman_list[length - 1] == 'I':
                    integer -= roman_dict[roman_list[length - 1]]
                    length -= 2
                else:
                    length -= 1
            else:
                length -= 1
        return integer

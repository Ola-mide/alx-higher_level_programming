#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = (number - ((number // 10) * 10))
        print("{}".format(last_digit), end='')
    else:
        last_digit = (-number - ((-number // 10) * 10))
        print("{}".format(last_digit), end='')
    return last_digit

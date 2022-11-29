#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
            count += 1
            i += 1
        except IndexError:
            print("\n", end="")
            return count
    print("\n", end="")
    return count

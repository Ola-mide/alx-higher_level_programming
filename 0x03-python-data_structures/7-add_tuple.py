#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = len(tuple_a)
    second = len(tuple_b)
    a = 0
    b = 0

    if first >= 2:
        a += tuple_a[0]
        b += tuple_a[1]
    elif first == 1:
        a += tuple_a[0]

    if second >= 2:
        a += tuple_b[0]
        b += tuple_b[1]
    elif second == 1:
        a += tuple_b[0]

    new_tuple = (a, b)
    return new_tuple

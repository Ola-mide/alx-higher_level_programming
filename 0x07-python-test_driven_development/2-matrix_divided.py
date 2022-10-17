#!/usr/bin/python3
"""
A module that divides the entries of a matrix by a specific integer
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    A function that divides matrix entries by div
    """
    for row in matrix:
        for num in row:
            if type(num) != int and type(num) != tuple:
                m = "matrix must be a matrix (List of lists) of integer/floats"
                raise TypeError(m)

    a = len(matrix)
    for b in range(a - 1):
        if len(matrix[b]) != len(matrix[b + 1]):
            m = "Each row of the matrix must have the same size"
            raise TypeError(m)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mtx = []
    idx = 0
    for row in matrix:
        mtx.append([])
        for num in row:
            mtx[idx].append(round(num / div, 2))
        idx += 1
    return mtx

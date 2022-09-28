#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[entry ** 2 for entry in row] for row in matrix]
    return square_matrix

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for entry in row:
            if entry == row[len(row) - 1]:
                print("{:d}".format(entry), end='')
            else:
                print("{:d}".format(entry), end=' ')
        print()

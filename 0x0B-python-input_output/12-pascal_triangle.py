#!/usr/bin/python3
"""
Module that generates a list of lists representing the Pascal's triangle
"""


def pascal_triangle(n):
    """
    A function that generates a list of lists
    representing the Pascal's triangle

    Args:
        n (int): max number
    """
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):
            if i == 0:
                pascal = []
                pascal.append(1)
                triangle.append(pascal)
            else:
                pascal = [1]
                if len(triangle[i - 1]) > 1:
                    pascal = [1]
                    idx = 1
                    while idx < len(triangle[i - 1]):
                        item = triangle[i - 1][idx] + triangle[i - 1][idx - 1]
                        pascal.append(item)
                        idx += 1
                pascal.append(1)
                triangle.append(pascal)
        return triangle

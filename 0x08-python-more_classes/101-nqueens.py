#!/usr/bin/python3
"""
Module for the N queens puzzle
"""
import sys


def queens(args):
    """
    A function that solves the queens puzzle

    Args:
        n (int): size of chessboard
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(args[1])
    if type(n) != int:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    print(n)


queens(sys.argv)

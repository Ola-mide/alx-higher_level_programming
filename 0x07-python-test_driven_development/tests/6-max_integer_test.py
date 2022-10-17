#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A module that tests the max_integer function
    """
    def test_max_integer(self):
        """
        A method that checks for the correct output
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([5]), 5)


if __name__ == "__main__":
    unittest.main()

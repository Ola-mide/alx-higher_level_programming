#!/usr/bin/python3
"""Update method test module"""
import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class TestUpdate(unittest.TestCase):
    """Update method test class"""
    def test_update_rectangle_args(self):
        """Testing Rectangle instance attributes after updating with *args"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_rectangle_kwargs(self):
        """
        Testing Rectangle instance attributes after updating with *kwargs
        """
        r2 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r2.update(height=1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r2.update(width=1, x=2)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_square_args(self):
        """Testing Square instance attributes after updating with *args"""
        s1 = Square(10, 0, 0, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 10")
        s1.update(89, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/0 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_square_kwargs(self):
        """
        Testing Square instance attributes after updating with *kwargs
        """
        s2 = Square(10, 0, 0, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 0/0 - 10")
        s2.update(x=12)
        self.assertEqual(s2.__str__(), "[Square] (1) 12/0 - 10")
        s2.update(size=7, y=1)
        self.assertEqual(s2.__str__(), "[Square] (1) 12/1 - 7")
        s2.update(size=7, id=89, y=1)
        self.assertEqual(s2.__str__(), "[Square] (89) 12/1 - 7")

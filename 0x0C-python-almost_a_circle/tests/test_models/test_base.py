#!/usr/bin/python3
"""Base Test module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base Test class"""
    b1 = Base()
    b2 = Base()
    b3 = Base(12)
    b4 = Base()
    b5 = Base(41)

    def test_instance_without_id_given(self):
        """Testing created instances without the id value"""
        self.assertIsInstance(TestBase.b1, Base)
        self.assertIsInstance(TestBase.b2, Base)
        self.assertIsInstance(TestBase.b4, Base)

    def test_instance_with_id_given(self):
        """Testing created instances with the id vcalue given"""
        self.assertIsInstance(TestBase.b3, Base)
        self.assertIsInstance(TestBase.b5, Base)

    def test_id_without_id_given(self):
        """Testing the id value for instances created without it"""
        self.assertEqual(TestBase.b1.id, 1)
        self.assertEqual(TestBase.b2.id, 2)
        self.assertEqual(TestBase.b4.id, 3)

    def test_id_with_id_given(self):
        """Testing the id value for instances created with it"""
        self.assertEqual(TestBase.b3.id, 12)
        self.assertEqual(TestBase.b5.id, 41)

#!/usr/bin/python3
"""Square Test module"""
import unittest
from models.base import *
from models.square import *


class TestSquare(unittest.TestCase):
    """Square Test class"""
    def test_instance_without_id_given(self):
        """Testing created instances withoud id value"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)
        self.assertIsInstance(s3, Square)

    def test_instance_with_id_given(self):
        """Testing created instances with id value"""
        s4 = Square(3, 1, 3, 6)
        self.assertIsInstance(s4, Square)

    def test_id_without_id_given(self):
        """Testing id value for instances created without it"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.id, 35)
        self.assertEqual(s2.id, 36)
        self.assertEqual(s3.id, 37)

    def test_id_with_id_given(self):
        """Testing id value for instances created with it"""
        s4 = Square(3, 1, 3, 6)
        self.assertEqual(s4.id, 6)

    def test_size(self):
        """Testing the size value"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(3, 1, 3, 6)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s4.size, 3)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, "6"
                               )
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -10
                               )

    def test_x(self):
        """Testing the x value"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(3, 1, 3, 6)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s4.x, 1)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 6, "4"
                               )
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 10, -5
                               )

    def test_y(self):
        """Testing the y value"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(3, 1, 3, 6)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s4.y, 3)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 6, 5, "3"
                               )
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 10, 30, -7
                               )

    def test_area(self):
        """Testing the area of each Square instance"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(3, 1, 3, 6)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s4.area(), 9)

    def test_str(self):
        """Testing the return value of the __str__ method"""
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(3, 1, 3, 6)
        s1_str = "[Square] (46) 0/0 - 5"
        s2_str = "[Square] (47) 2/0 - 2"
        s3_str = "[Square] (48) 1/3 - 3"
        s4_str = "[Square] (6) 1/3 - 3"
        self.assertEqual(s1.__str__(), s1_str)
        self.assertEqual(s2.__str__(), s2_str)
        self.assertEqual(s3.__str__(), s3_str)
        self.assertEqual(s4.__str__(), s4_str)

    def test_to_dictionary(self):
        """Testing the dictionary representation of Square"""
        s1 = Square(10, 2, 1, 9)
        s1_dict = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        s2 = Square(1, 1, 0, 10)
        s2_dict = {'id': 10, 'x': 1, 'size': 1, 'y': 0}
        self.assertEqual(s1.to_dictionary(), s1_dict)
        self.assertEqual(s2.to_dictionary(), s2_dict)
        s2.update(**s1_dict)
        self.assertEqual(s2.to_dictionary(), s1_dict)

    def test_to_json_string(self):
        """Testing json string from square dict"""
        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        s1_json_str = '[{"id": 8, "size": 10, "x": 7, "y": 2}]'
        self.assertEqual(Base.to_json_string([dictionary]), s1_json_str)

    def test_save_to_file(self):
        """Testing json rep saved to file"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 0, 1)
        Square.save_to_file([s1, s2])
        stf = '[{"id": 8, "size": 10, "x": 7, "y": 2}, '\
            '{"id": 1, "size": 2, "x": 4, "y": 0}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read().__str__(), stf)

    def test_from_json_string(self):
        """Testing expected list from json string"""
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
            ]
        json_list_input = Square.to_json_string(list_input)
        output = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
            ]
        self.assertEqual(Square.from_json_string(json_list_input), output)

    def test_create(self):
        """Testing the creation of an instance"""
        s1 = Square(3, 5, 1, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.__str__(), "[Square] (1) 5/1 - 3")

    def test_load_from_file(self):
        """Testing instances created from a file"""
        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        output = Square.load_from_file()
        for instance in output:
            self.assertIsInstance(instance, Square)
        self.assertEqual(output[0].__str__(), s1.__str__())
        self.assertEqual(output[1].__str__(), s2.__str__())

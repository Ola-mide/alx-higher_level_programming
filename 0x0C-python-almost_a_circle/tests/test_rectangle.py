#!/usr/bin/python3
"""Rectangle Test module"""
import unittest
from models.base import *
from models.rectangle import *
import io
import sys


class TestRectangle(unittest.TestCase):
    """Rectangle Test class"""
    def test_instance_without_id_given(self):
        """Testing created instances without id value"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)

    def test_instance_with_id_given(self):
        """Testing created instances with id value"""
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertIsInstance(r3, Rectangle)

    def test_id_without_id_given(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        """Testing id value for instances created without it"""
        self.assertEqual(r1.id, 14)
        self.assertEqual(r2.id, 15)

    def test_id_with_id_given(self):
        r3 = Rectangle(8, 7, 5, 1, 12)
        """Testing id value for instances created with it"""
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Testing the width value"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 8)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "6", 5
                               )
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -10, 30
                               )
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, 0, 30
                               )

    def test_height(self):
        """Testing the height value"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 7)
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 10, "2"
                               )
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 10, -4
                               )
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 10, 0
                               )

    def test_x(self):
        """Testing the x value"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.x, 5)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 6, 5, "4"
                               )
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 10, 30, -5
                               )

    def test_y(self):
        """Testing the y value"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 1)
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 6, 5, 4, "3"
                               )
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 10, 30, 5, -7
                               )

    def test_area(self):
        """Testing the area of each Rectangle instance"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Testing the display output"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(3, 2, 1)
        r3 = Rectangle(3, 2, 1, 1, 3)
        output1 = io.StringIO()
        sys.stdout = output1
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output1.getvalue(), "###\n###\n")
        output2 = io.StringIO()
        sys.stdout = output2
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output2.getvalue(), " ###\n ###\n")
        output3 = io.StringIO()
        sys.stdout = output3
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output3.getvalue(), "\n ###\n ###\n")

    def test_str(self):
        """Testing the return value of the __str__ method"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 5, 1, 12)
        r1_str = "[Rectangle] (20) 0/0 - 3/2"
        r2_str = "[Rectangle] (21) 0/0 - 2/10"
        r3_str = "[Rectangle] (12) 5/1 - 8/7"
        self.assertEqual(r1.__str__(), r1_str)
        self.assertEqual(r2.__str__(), r2_str)
        self.assertEqual(r3.__str__(), r3_str)

    def test_to_dictionary(self):
        """Testing the dictionary representation of Rectangle"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r2 = Rectangle(1, 1, 0, 0, 2)
        r2_dict = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(r1.to_dictionary(), r1_dict)
        self.assertEqual(r2.to_dictionary(), r2_dict)
        r2.update(**r1_dict)
        self.assertEqual(r2.to_dictionary(), r1_dict)

    def test_to_json_string(self):
        """Testing json string from rectangle dict"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        r1_json_str = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string([dictionary]), r1_json_str)

    def test_save_to_file(self):
        """Testing json rep saved to file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        stf = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '\
            '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), stf)
        Rectangle.save_to_file(None)
        stf = '[]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), stf)
        Rectangle.save_to_file([])
        stf = '[]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read().__str__(), stf)

    def test_from_json_string(self):
        """Testing expected list from json string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        output = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        self.assertEqual(Rectangle.from_json_string(json_list_input), output)

    def test_create(self):
        """Testing the creation of an instance"""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

    def test_load_from_file(self):
        """Testing instances created from a file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        output = Rectangle.load_from_file()
        for instance in output:
            self.assertIsInstance(instance, Rectangle)
        self.assertEqual(output[0].__str__(), r1.__str__())
        self.assertEqual(output[1].__str__(), r2.__str__())

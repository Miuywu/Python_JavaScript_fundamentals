#!/usr/bin/python3

"""
Unittesting for task 0 - Base
models/base.py
"""

import sys
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """Class Base unittests"""


    def test_base0_normal(self):
        """tests for task 1"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

        base0 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(type(base0), Base)
        self.assertEqual(isinstance(base0, Base), True)

    def test_base0_input(self):
        """Test for task 1"""
        base0 = Base(46)
        self.assertEqual(base0.id, 46)

    def test_base0_neg(self):
        """Test for task 1"""
        base0 = Base(-46)
        self.assertEqual(base0.id, -46)

    def test_base0_None(self):
        """Test for task 1"""
        base0 = Base(None)
        self.assertEqual(base0.id, 1)

    def test_base0_zero(self):
        """Test for task 1"""
        base0 = Base(0)
        self.assertEqual(base0.id, 0)

    def test_base0_str(self):
        """Test for task 1"""
        base0 = Base('str')
        self.assertEqual(base0.id, 'str')

    def test_base0_list(self):
        """Test for task 1"""
        base0 = Base(['l', 'i', 's', 't'])
        self.assertEqual(base0.id, ['l', 'i', 's', 't'])

    def test_base0_tuple(self):
        """Test for task 1"""
        base0 = Base((1, 2))
        self.assertEqual(base0.id, (1, 2))

    def test_base0_dict(self):
        """Test for task 1"""
        base0 = Base({'d': 'i', 'c': 't'})
        self.assertEqual(base0.id, {'d': 'i', 'c': 't'})

    def test_base0_dict(self):
        """Test for task 1"""
        base0 = Base({'d': 'i', 'c': 't'})
        self.assertEqual(base0.id, {'d': 'i', 'c': 't'})
#------------------------------------------------------------
    def test_base15_(self):
        """Test for task 15"""
        base0 = Base({'d': 'i', 'c': 't'})
        self.assertEqual(base0.id, {'d': 'i', 'c': 't'})

    def test_load_from_file(self):
        """Test load_from_file"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()

        Rectangle.save_to_file([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file()
        Square.save_to_file([s1, s2, s3])
        list_objs_s = Square.load_from_file()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)


if __name__ == '__main__':
    unittest.main()

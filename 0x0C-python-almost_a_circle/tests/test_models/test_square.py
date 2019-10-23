#!/usr/bin/python3
"""Unittest for Square Size
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

-ed:
class TestSquareSize(unittest.TestCase):
    """Test Square Size Method"""
    def test_size(self):
        s1 = Square(5)
          self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test1_inputs(self):
        """square valid input"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test2_inputs(self):
        """square negative input"""
        self.assertRaises(ValueError, Square, -5)

    def test3_inputs(self):
        """square string input"""
        self.assertRaises(TypeError, Square, "five")

    def test4_inputs(self):
        """square list input"""
        self.assertRaises(TypeError, Square, [69, 619])

    def test5_inputs(self):
        s2 = Square(6)

    def test6_updates(self):
        s3 = Square(3)
        s3.update(69)
        self.assertEqual(s3.id, 69)

    def test7_updates(self):
        """check if updates kwargs"""

    def test8_updates(self):
        s5 = Square(1, 2, 3, 4)

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        r = Square(1, 1, 1, 1)
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)

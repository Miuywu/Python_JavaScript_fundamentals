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

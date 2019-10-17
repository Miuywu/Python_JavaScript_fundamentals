#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestStringMethods(unittest.TestCase):

    def test_start(self):
        self.assertEqual(max_integer([7, 5, 6, 7]), 7)

    def test_mid(self):
        self.assertEqual(max_integer([5, 6, 5]), 6)

    def test_neg(self):
        self.assertEqual(max_integer([5, -6, 7]), 7)

    def test_neg_all(self):
        self.assertEqual(max_integer([-5, -6, -7]), -5)

    def test_normal(self):
        self.assertEqual(max_integer([5, 6, 7]), 7)

    def test_len(self):
        list = [5, 6, 7]
        copy = list.copy()
        self.assertEqual(max_integer([5, 6, 7]), 7)
        self.assertEqual(len(list), len(copy))
        for a in range(len(list)):
            self.assertEqual(list[a], copy[a])

    def test_duplicate(self):
        self.assertEqual(max_integer([5, 6, 7, 7]), 7)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()

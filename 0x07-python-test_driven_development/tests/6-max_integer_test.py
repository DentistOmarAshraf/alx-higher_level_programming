#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([0, 1, 2, 4]), 4)
        self.assertAlmostEqual(max_integer([30, 10, 55, -1]), 55)
        self.assertAlmostEqual(max_integer([100, 97, 90, 22]), 100)
        self.assertAlmostEqual(max_integer([-1, -3, -50, -10]), -1)
        self.assertAlmostEqual(max_integer([10]), 10)
        self.assertAlmostEqual(max_integer([]), None)

#!/usr/bin/python3
"""Testing Class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Rectangle Class Tests"""
    def test_const(self):
        """Testing instance creation"""
        a = Rectangle(10, 20)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 20)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 1)

    def test_const_two(self):
       """Testing instance creation"""
       b = Rectangle(10, 20, 2)
       self.assertEqual(b.width, 10)
       self.assertEqual(b.height, 20)
       self.assertEqual(b.x, 2)
       self.assertEqual(b.y, 0)
       self.assertEqual(b.id, 2)


if __name__ == "__main__":
    unittest.main()

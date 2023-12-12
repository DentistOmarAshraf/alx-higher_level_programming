#!/usr/bin/python3
"""Testing Class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Testing Rectangle class"""
    def test_const(self):
        """Testing instance crestion"""
        a = Rectangle(10, 20)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 20)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 3)

    def test_const_two(self):
        """Testing instance crestion"""
        b = Rectangle(10, 20, 2)
        self.assertEqual(b.width, 10)
        self.assertEqual(b.height, 20)
        self.assertEqual(b.x, 2)
        self.assertEqual(b.y, 0)
        self.assertEqual(b.id, 5)

    def test_const_there(self):
        """Testing instance crestion"""
        c = Rectangle(10, 20, 2, 3)
        self.assertEqual(c.width, 10)
        self.assertEqual(c.height, 20)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 3)
        self.assertEqual(c.id, 4)

    def test_const_four(self):
        """Testing instance crestion"""
        d = Rectangle(10, 20, 3, 2, 100)
        self.assertEqual(d.width, 10)
        self.assertEqual(d.height, 20)
        self.assertEqual(d.x, 3)
        self.assertEqual(d.y, 2)
        self.assertEqual(d.id, 100)


if __name__ == "__main__":
    unittest.main()

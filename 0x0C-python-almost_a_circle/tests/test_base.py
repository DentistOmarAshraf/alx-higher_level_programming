#!/usr/bin/python3
"""Testing models.base"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """Base Class Tests"""
    def test_id(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base(20)
        self.assertEqual(c.id, 20)
        c1 = Base({"name": "omar"})
        self.assertEqual(c1.id, {"name": "omar"})

    def test_err(self):
        with self.assertRaises(TypeError):
            d = Base(20, 10)
        """
        The Next Tests for Validator in Base class
        (Rectangle) Class inherits from (Base)
        Base.width_height_validator
        """
        with self.assertRaises(TypeError):
            e = Rectangle("a", 10)
        with self.assertRaises(TypeError):
            f = Rectangle(10, "b")
        with self.assertRaises(ValueError):
            g = Rectangle(0, 0)
        """
        Next -> Base.x_y_validator
        """
        with self.assertRaises(TypeError):
            h = Rectangle(10, 20, "o", 1)
        with self.assertRaises(TypeError):
            i = Rectangle(10, 20, 3, "o")
        with self.assertRaises(ValueError):
            j = Rectangle(10, 20, -1, 5)
        with self.assertRaises(ValueError):
            k = Rectangle(10, 20, 5, -1)

    def test_method(self):
        """
        testing Base.to_json_string()
        """
        self.assertEqual(Base.to_json_string([1, 2, 3]), "[1, 2, 3]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_method_err(self):
        """testing Base.to_json_string() error raises"""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])
    
    def test_method2(self):
        """
        testing Base.from_json_string()
        """
        self.assertEqual(Base.from_json_string("[1, 2, 3]"), [1, 2, 3])
        self.assertEqual(Base.from_json_string('{"name":"omar"}'), {"name": "omar"})
        self.assertEqual(Base.from_json_string(None), [])

    def test_method2_err(self):
        """Testing Base.from_json_string error raises"""
        with self.assertRaises(TypeError):
            Base.from_json_string("o", "n")
        with self.assertRaises(TypeError):
            Base.from_json_string()

if __name__ == "__main__":
    unittest.main()

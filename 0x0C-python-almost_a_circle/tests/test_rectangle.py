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

    def test_const_err(self):
        """Validator test"""
        with self.assertRaises(TypeError):
            x = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            x = Rectangle(1, "2")

    def test_method(self):
        """testing __str__() method"""
        e = Rectangle(20, 10, 1, 5, 600)
        string = "[Rectangle] (600) 1/5 - 20/10"
        self.assertEqual(e.__str__(), string)
        f = Rectangle(30, 40)
        string = "[Rectangle] (6) 0/0 - 30/40"
        self.assertEqual(f.__str__(), string)

    def test_method_two(self):
        """testing area() method"""
        g = Rectangle(4, 8)
        self.assertEqual(g.area(), 32)
        h = Rectangle(17, 2)
        """method Error"""
        with self.assertRaises(TypeError):
            h.area(1)
        with self.assertRaises(TypeError):
            h.area(10, 20)

    def test_method_three(self):
        """testing to_dictionary() method"""
        i = Rectangle(1, 2, 3, 4, 94)
        dic = {"x": 3, "y": 4, "id": 94, "height": 2, "width": 1}
        self.assertEqual(i.to_dictionary(), dic)
        i = Rectangle(1, 1)
        dic = {"x": 0, "y": 0, "id": 7, "height": 1, "width": 1}
        self.assertEqual(i.to_dictionary(), dic)
        """method Error"""
        with self.assertRaises(TypeError):
            i.to_dictionary(1, 2)


if __name__ == "__main__":
    unittest.main()

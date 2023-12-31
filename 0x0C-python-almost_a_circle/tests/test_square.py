#!/usr/bin/python3
"""Testing Class Square"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
import os


class Test_Square(unittest.TestCase):
    """Testing Square class"""
    def test_const_zero(self):
        """Testing instance creation"""
        a = Square(1)
        self.assertEqual(a.size, 1)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 1)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 13)

    def test_const_one(self):
        """Testing instance creation"""
        b = Square(2, 1)
        self.assertEqual(b.size, 2)
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 0)
        self.assertEqual(b.id, 11)

    def test_const_two(self):
        """Testing instance creation"""
        c = Square(4, 1, 3)
        self.assertEqual(c.size, 4)
        self.assertEqual(c.x, 1)
        self.assertEqual(c.y, 3)
        self.assertEqual(c.id, 12)

    def test_const_three(self):
        """Testing instance creation"""
        d = Square(10, 7, 4, 943)
        self.assertEqual(d.size, 10)
        self.assertEqual(d.x, 7)
        self.assertEqual(d.y, 4)
        self.assertEqual(d.id, 943)

    def test_const_err(self):
        """Testing instance error raises"""
        with self.assertRaises(TypeError):
            e = Square("1")
        with self.assertRaises(TypeError):
            e = Square(2, "3")
        with self.assertRaises(TypeError):
            e = Square(3, 3, "4")
        with self.assertRaises(ValueError):
            e = Square(-1)
        with self.assertRaises(ValueError):
            e = Square(2, -1)
        with self.assertRaises(ValueError):
            e = Square(2, 1, -1)
        with self.assertRaises(TypeError):
            e = Square()
        with self.assertRaises(TypeError):
            e = Square(1, 2, 3, 4, 32)
        with self.assertRaises(ValueError):
            e = Square(0)

    def test_method_zero(self):
        """Testing method Square.__str__()"""
        string = "[Square] (94) 2/3 - 1"
        f = Square(1, 2, 3, 94)
        self.assertEqual(f.__str__(), string)
        string = "[Square] (18) 0/0 - 1"
        g = Square(1)
        self.assertEqual(g.__str__(), string)
        string = "[Square] (19) 3/0 - 2"
        h = Square(2, 3)
        self.assertEqual(h.__str__(), string)
        string = "[Square] (20) 4/5 - 2"
        i = Square(2, 4, 5)
        self.assertEqual(i.__str__(), string)
        """Testing Error"""
        with self.assertRaises(TypeError):
            i.__str__(12)

    def test_method_one(self):
        """Testing method Square.update()"""
        j = Square(1, 0, 0, 400)
        j.update(314)
        self.assertEqual(j.id, 314)
        j.update(314, 2)
        self.assertEqual(j.size, 2)
        j.update(314, 2, 4)
        self.assertEqual(j.x, 4)
        j.update(314, 2, 4, 5)
        self.assertEqual(j.y, 5)
        j.update(id=412)
        self.assertEqual(j.id, 412)
        j.update(id=412, size=80)
        self.assertEqual(j.size, 80)
        j.update(id=412, size=18, x=45)
        self.assertEqual(j.id, 412)
        self.assertEqual(j.size, 18)
        self.assertEqual(j.x, 45)
        j.update(id=412, size=18, x=45, y=3)
        self.assertEqual(j.id, 412)
        self.assertEqual(j.size, 18)
        self.assertEqual(j.x, 45)
        self.assertEqual(j.y, 3)
        j.update(y=73)
        self.assertEqual(j.y, 73)

    def test_method_two(self):
        """Testing method Square.to_dictionary()"""
        dic = {"id": 22, "x": 4, "size": 3, "y": 0}
        k = Square(3, 4, 0, 22)
        self.assertEqual(k.to_dictionary(), dic)
        dic = {"id": 21, "x": 0, "size": 2, "y": 1}
        lm = Square(2, 0, 1, 21)
        self.assertEqual(lm.to_dictionary(), dic)
        """method Error"""
        with self.assertRaises(TypeError):
            lm.to_dictionary(2)

    def test_more_one(self):
        """This Is Additional Tests Added
        for Base(), Rectangle() and Square()"""
        self.assertEqual(Base.from_json_string("[]"), [])
        arr = [{"id": 89}]
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), arr)

        n = Rectangle(2, 3, 4)
        string = "    ##\n    ##\n    ##\n"
        with patch('sys.stdout', new=StringIO()) as dis:
            n.display()
            self.assertEqual(dis.getvalue(), string)

    def test_more_two(self):
        """Testing create() method in Base Class"""
        dic = {"id": 89, "width": 30, "height": 40}
        x = Rectangle.create(**dic)
        self.assertEqual(x.width, 30)
        self.assertEqual(x.height, 40)
        self.assertEqual(x.id, 89)

        dic = {"id": 89, "width": 30}
        n = Rectangle.create(**dic)
        self.assertEqual(n.id, 89)
        self.assertEqual(n.width, 30)

        dic = {"id": 89}
        h = Rectangle.create(**dic)
        self.assertEqual(h.id, 89)

        dic = {"id": 89, "width": 23, "height": 40, "x": 10}
        z = Rectangle.create(**dic)
        self.assertEqual(z.id, 89)
        self.assertEqual(z.width, 23)
        self.assertEqual(z.height, 40)
        self.assertEqual(z.x, 10)

        dic = {"id": 89, "width": 32, "height": 13, "x": 12, "y": 24}
        m = Rectangle.create(**dic)
        self.assertEqual(m.id, 89)
        self.assertEqual(m.width, 32)
        self.assertEqual(m.height, 13)
        self.assertEqual(m.x, 12)
        self.assertEqual(m.y, 24)

        dic = {}
        mi = Rectangle.create(**dic)
        self.assertEqual(mi.width, 1)
        self.assertEqual(mi.height, 1)
        self.assertEqual(mi.x, 0)
        self.assertEqual(mi.y, 0)
        self.assertEqual(mi.id, 32)

    def test_more_three(self):
        """Testing Creart() method"""
        dic = {"id": 90}
        a1 = Square.create(**dic)
        self.assertEqual(a1.id, 90)

        dic = {"id": 91, "size": 14}
        a2 = Square.create(**dic)
        self.assertEqual(a2.id, 91)
        self.assertEqual(a2.size, 14)

        dic = {"id": 92, "size": 20, "x": 10}
        a3 = Square.create(**dic)
        self.assertEqual(a3.id, 92)
        self.assertEqual(a3.size, 20)
        self.assertEqual(a3.x, 10)

        dic = {"id": 98, "size": 15, "x": 3, "y": 1}
        a4 = Square.create(**dic)
        self.assertEqual(a4.id, 98)
        self.assertEqual(a4.size, 15)
        self.assertEqual(a4.x, 3)
        self.assertEqual(a4.y, 1)

        dic = {}
        a5 = Square.create(**dic)
        self.assertEqual(a5.size, 1)
        self.assertEqual(a5.x, 0)
        self.assertEqual(a5.y, 0)
        self.assertEqual(a5.id, 26)

        with self.assertRaises(TypeError):
            a6 = Square.create({},{})

    def test_creation(self):
        """Testing File Creation method in Base class"""
        with open("Rectangle.json", "a+", encoding="utf-8") as f:
            pass
        Rectangle.save_to_file(None)
        
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = f.read()
        
        self.assertEqual(data, "[]")
        
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = f.read()

        self.assertEqual(data, "[]")
        
        z = Rectangle(4, 3)
        Rectangle.save_to_file([z])
        string = '[{"x": 0, "y": 0, "id": 14, "height": 3, "width": 4}]'
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            data = f.read()

        self.assertEqual(data, string)
        os.remove('Rectangle.json')

        arr = Rectangle.load_from_file()
        self.assertEqual(arr, [])

        Rectangle.save_to_file([z])
        arr = Rectangle.load_from_file()
        self.assertIsInstance(arr[0], Rectangle)
        os.remove('Rectangle.json')

    def test_creationTwo(self):
        """Testing file creation and testing data inside the file"""
        with open("Square.json", "a+", encoding="utf-8") as f:
            pass

        Square.save_to_file([])

        with open("Square.json", "r", encoding="utf-8") as f:
            data = f.read()

        self.assertEqual(data, "[]")

        z = Square(1)
        Square.save_to_file([z])
        string ='[{"id": 16, "x": 0, "size": 1, "y": 0}]'
        with open("Square.json", "r", encoding="utf-8") as f:
            data = f.read()

        self.assertEqual(data, string)
        os.remove('Square.json')
        arr = Square.load_from_file()
        self.assertEqual(arr, [])

        Square.save_to_file([z])
        arr = Square.load_from_file()
        self.assertIsInstance(arr[0], Square)
        os.remove('Square.json')

    def test_creationthree(self):
        """Testing file creation and testing data inside"""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            data = f.read()
        self.assertEqual(data, "[]")
        os.remove('Square.json')


if __name__ == "__main__":
    unittest.main()

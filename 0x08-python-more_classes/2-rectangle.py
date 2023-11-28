#!/usr/bin/python3
"""Agin Rectangle class
>>> my = Rectangle(-1, 10)
Traceback (most recent call last):
    ...
ValueError: width must be >= 0
>>> my = Rectangle("oamr", 10)
Traceback (most recent call last):
    ...
TypeError: width must be an integer
>>> my = Rectangle(10, -1)
Traceback (most recent call last):
    ...
ValueError: height must be >= 0
>>> my = Rectangle(10, "omar")
Traceback (most recent call last):
    ...
TypeError: height must be an integer
>>> my = Rectangle(2, 4)
>>> my.area()
8
>>> my.perimeter()
12
>>> my.width = 0
>>> my.height = 2
>>> my.area()
0
>>> my.perimeter()
0
"""


class Rectangle:
    """Rectangle has 4 lines and 4 angle 90 degree"""

    def __init__(self, width=0, height=0):
        """Constructor Function
        Args:
            param1(self): instance
            param2(width): int must be integer and >= 0
            param3(height): int must be integer and >= 0
        Return:
            None
        """
        self.height = height
        self.width = width

    def area(self):
        """Rectangle area
        Args:
            param1(self): instance
        Return:
            area of triangle
        """
        return self.height * self.width

    def perimeter(self):
        """Rectange perimeter
        Args:
            param1(self): instance
        Return:
            perimeter(int)
        """
        if self.height and self.width:
            return (self.height + self.width) * 2
        return 0

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

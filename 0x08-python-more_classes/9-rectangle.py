#!/usr/bin/python3
"""Agin Rectangle class"""


class Rectangle:
    """Rectangle has 4 lines and 4 angle 90 degree"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Draw rectangle
        Args:
            param1(self): instance
        Return:
            str(draw)
        """
        rec = """"""
        if self.width == 0 or self.height == 0:
            return rec
        for i in range(self.height):
            for j in range(self.width):
                if isinstance(self.print_symbol, str):
                    rec += self.print_symbol
                else:
                    rec += str(self.print_symbol)
            if i != self.height - 1:
                rec += '\n'
        return rec

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """return represntaion of instanc"""
        return f"Rectangle({self.width}, {self.height})"

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function return instance which is bigger
        Args:
            param1(rect_1): instance
            param2(rect_2): instance
        Return:
            instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        x = rect_1.area()
        y = rect_2.area()
        if x > y or x == y:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(size, size)

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

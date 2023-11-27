#!/usr/bin/python3
"""This is About Rectangle Class"""


class Rectangle:
    """class About foken Rect"""

    def __init__(self, width, height):
        """constructor function
        Args:
            param1(self): instance
            param2(width): must int must >= 0
            param3(height): must int must >= 0
        Return: None
        """

        self.height = height
        self.width = width

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

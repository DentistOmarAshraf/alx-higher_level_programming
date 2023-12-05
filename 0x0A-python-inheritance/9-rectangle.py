#!/usr/bin/python3
"""
Rectangle Class inherits BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        constructor function
        Args:
            param1(self): instance
            param2(width): must be int and > 0
            param3(height): must be int and > 0
        """
        super().integer_validator('height', height)
        super().integer_validator('width', width)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        function return str represent the instance
        """
        string = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return (string)

    def area(self):
        """
        function return the width of rectangle instance
        """
        return self.__width * self.__height

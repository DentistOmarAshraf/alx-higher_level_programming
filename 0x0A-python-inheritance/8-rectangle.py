#!/usr/bin/python3
"""
Rectangele class Inherits BaseGeometry task 7
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class inherits BaseGeometry"""

    def __init__(self, width, height):
        """
        Constructor function
        Args:
            param1(self): instance
            param2(width): must be integer and > 0
            param3(height): must be integer and > 0
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

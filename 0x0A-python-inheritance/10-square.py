#!/usr/bin/python3
"""
Square class inherits super Rectangle
>>> s = Square(13)
>>> print(s)
[Rectangle] 13/13
>>> print(s.area())
169
>>> s = Square("oamr")
Traceback (most recent call last):
    ...
TypeError: size must be an integer
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits Rectangle"""

    def __init__(self, size):
        """
        Constructor Function
        """
        super().integer_validator('size', size)
        super().__init__(size, size)

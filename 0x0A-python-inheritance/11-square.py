#!/usr/bin/python3
"""
Square class inherits super Rectangle
>>> s = Square(13)
>>> print(s)
[Square] 13/13
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
        self.__size = size

    def __str__(self):
        """
        Return string represent the instance
        """
        string = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return string

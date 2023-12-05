#!/usr/bin/python3
"""
Square class inherits super Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits Rectangle"""

    def __init__(self, size):
        """
        Constructor Function
        """
        super().__init__(size, size)

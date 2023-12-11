#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor Function"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        super().width_height_validator('width', size)
        self.__size = size

    def __str__(self):
        """String represatation"""
        string = "[Square] ({}) ".format(self.id)
        string += "{}/{} - {}".format(self.x, self.y, self.size)
        return string

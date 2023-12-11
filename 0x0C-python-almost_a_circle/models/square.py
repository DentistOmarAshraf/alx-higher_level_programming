#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor Function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().width_height_validator('width', value)
        self.width = value
        self.height = value

    def __str__(self):
        """String represatation"""
        string = "[Square] ({}) ".format(self.id)
        string += "{}/{} - {}".format(self.x, self.y, self.width)
        return string

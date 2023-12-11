#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor Function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String represatation"""
        string = "[Square] ({}) ".format(self.id)
        string += "{}/{} - {}".format(self.x, self.y, self.width)
        return string

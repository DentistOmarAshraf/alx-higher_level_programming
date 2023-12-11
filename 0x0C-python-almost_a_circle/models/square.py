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

    def update(self, *args, **kwargs):
        """function update square info"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.size = args[1]
            if i == 2:
                self.x = args[2]
            if i == 3:
                self.y = args[3]
        if len(args) == 0:
            if "size" in kwargs.keys():
                self.size = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
            if "id" in kwargs.keys():
                self.id = kwargs["id"]

    def to_dictionary(self):
        """set a dictionary for square"""
        new = {}
        new["id"] = self.id
        new["x"] = self.x
        new["size"] = self.size
        new["y"] = self.y
        return new

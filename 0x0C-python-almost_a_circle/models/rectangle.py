#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class inherets from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.width_height_validator('width', width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.width_height_validator('height', height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.x_y_validator('x', x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.x_y_validator('y', y)
        self.__y = y

    def width_height_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be > 0".format(name))
        self.name = name
        self.value = value

    def x_y_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        self.name = name
        self.value = value

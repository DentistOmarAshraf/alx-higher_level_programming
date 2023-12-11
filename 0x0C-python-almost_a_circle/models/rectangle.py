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
        super().width_height_validator('width', width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        super().width_height_validator('height', height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        super().x_y_validator('x', x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        super().x_y_validator('y', y)
        self.__y = y

    def __str__(self):
        """function return string represent of instance"""
        string = "[Rectangle] ({}) ".format(self.id)
        string += "{}/{} - ".format(self.x, self.y)
        string += "{}/{}".format(self.width, self.height)
        return string

    def update(self, *args):
        """update instance attribute"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

    def area(self):
        """Function to return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Function to print Rectangle in stdout"""
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

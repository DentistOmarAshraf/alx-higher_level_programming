#!/usr/bin/python3
"""Class base Module"""
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instance Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def width_height_validator(self, name, value):
        """
        function to validate values
        I Used this function in class Rectangle
        which Inherits class base
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be > 0".format(name))
        self.name = name
        self.value = value

    def x_y_validator(self, name, value):
        """
        function to validate x and y
        ALso as above I used it in class Rectangle
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        self.name = name
        self.value = value

    @staticmethod
    def to_json_string(list_dict):
        """function return List of dict to json string"""
        if list_dict is None:
            return "[]"
        return json.dumps(list_dict)

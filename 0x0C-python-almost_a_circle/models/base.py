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
    def from_json_string(string):
        """return a list of Json string reprsentation"""
        if string is not None:
            return json.loads(string)
        return []

    @staticmethod
    def to_json_string(list_dict):
        """function return List of dict to json string"""
        if list_dict is None:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_obj):
        """function to save info of Instance into file"""
        arr = []
        if list_obj is not None:
            for i in list_obj:
                arr.append(i.to_dictionary())
        fname = "{}.json".format(cls.__name__)

        with open(fname, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(arr))

    @classmethod
    def create(cls, **dic):
        """create instance from subclass"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)

        dum.update(**dic)
        return dum

    @classmethod
    def load_from_file(cls):
        """function to create instance from Json"""
        fname = "{}.json".format(cls.__name__)
        
        with open(fname, "r", encoding="utf-8") as f:
            ls = Base.from_json_string(f.read())

        arr = []
        for i in ls:
            arr.append(cls.create(**i))
        return arr

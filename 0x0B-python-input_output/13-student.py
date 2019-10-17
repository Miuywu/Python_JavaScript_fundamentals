#!/usr/bin/python3
class Student:
    """
    student
    """

    def __init__(self, first_name, last_name, age):
        """
        Init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        get dict
        """
        if attrs is None:
            return self.__dict__
        f_dict = {}
        for ki in attrs:
            if ki in self.__dict__.keys():
                f_dict[ki] = self.__dict__[ki]
        return f_dict

    def reload_from_json(self, json):
        """
        reloading
        """
        for ki in json:
            setattr(self, ki, json[ki])

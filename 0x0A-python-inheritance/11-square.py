#!/usr/bin/python3
"""create class square from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits Rectangle"""
    def __init__(self, size):
        """init square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def __str__(self):
        """[square] s/s"""
        return "[Square] " + "{}/{}".format(self.__size, self.__size)

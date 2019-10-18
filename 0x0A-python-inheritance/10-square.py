#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size * self.__size

#!/usr/bin/python3
class Square:
    """[] with size"""
    def __init__(self, size=0):
        """Init"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area"""
        return self.__size**2

    def my_print(self):
        """print []"""
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()

#!/usr/bin/python3
class Square:
    """[] with size"""
    def __init__(self, size=0, position=(0, 0)):
        """Init"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """print []"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for a in range(self.__size):
                for offset in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()

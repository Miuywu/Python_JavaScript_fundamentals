#!/usr/bin/python3

"""
Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructs a Rectangle"""

        super().__init__(id)

        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""

        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""

        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""

        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """area"""

        return self.__width * self.__height

    def display(self):
        """print []"""

        for c in range(self.__y):
            print()
        for a in range(self.__height):
            for d in range(self.__x):
                print(' ', end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[Rectangle] " + "({}) {}/{} - {}/{}".format(
self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates attributes to input args or kwargs"""

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args is not None:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                elif a == 1:
                    self.width = args[1]
                elif a == 2:
                    self.height = args[2]
                elif a == 3:
                    self.x = args[3]
                elif a == 4:
                    self.y = args[4]

    def to_dictionary(self):
        """Dict of Rectangle"""

        dic = {}
        for key, val in vars(self).items():
            if len(key) > 11:
                dic[key[12:]] = val
            else:
                dic[key] = val
        return dic

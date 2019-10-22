#!/usr/bin/python3

"""
Class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructs a square"""

        super().__init__(size, size, x, y, id)


    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """get size"""

        return self.width

    @size.setter
    def size(self, value):
        """Set size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update args kwargs"""

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args is not None:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                elif a == 1:
                    self.size = args[1]
                elif a == 2:
                    self.x = args[2]
                elif a == 3:
                    self.y = args[3]

    def to_dictionary(self):
        """Dict of Square"""

        dic = {}
        for key, val in vars(self).items():
            if len(key) > 12:
                if key[12:] == 'width' or key[12:] == 'height':
                    dic['size'] = val
                else:
                    dic[key[12:]] = val
            else:
                dic[key] = val
        return dic

#!/usr/bin/python3
"""

los commentos

"""


def add_integer(a, b=98):
    """
    mas commentos
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) != int:
        a = int(a)
    if type(b) != int:
        b = int(b)
    return a + b

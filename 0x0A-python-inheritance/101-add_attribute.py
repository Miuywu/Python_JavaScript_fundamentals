#!/usr/bin/python3
"""safely adds attr"""


def add_attribute(self, attr_k, attr_v):
    """Adds attr"""
    if hasattr(self, '__dict__') == False:
        raise TypeError("can't add new attribute")
    else:
        setattr(self, attr_k, attr_v)

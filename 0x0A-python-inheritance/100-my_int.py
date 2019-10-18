#!/usr/bin/python3
"""MyInt is int but '==' and '!=' operators inverted"""


class MyInt(int):
    """MyInt"""
    def __ne__(self, value):
        """"!= -> =="""
        return super().__eq__(value)
    def __eq__(self, value):
        """== -> !="""
        return super().__ne__(value)

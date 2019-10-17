#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    if len(tuple_a) is 1:
        a = tuple_a[0]
    b = 0
    if len(tuple_a) >= 2:
        a = tuple_a[0]
        b = tuple_a[1]
    c = 0
    if len(tuple_b) is 1:
        c = tuple_b[0]
    d = 0
    if len(tuple_b) >= 2:
        c = tuple_b[0]
        d = tuple_b[1]
    return (a + c, b + d)

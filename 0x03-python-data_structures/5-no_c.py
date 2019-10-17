#!/usr/bin/python3
def no_c(my_string):
    s = my_string
    c = 'c'
    counts = s.count(c)
    s = list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = '' . join(s)

    c = 'C'
    counts = s.count(c)
    s = list(s)
    while counts:
        s.remove(c)
        counts -= 1
    s = '' . join(s)

    return s

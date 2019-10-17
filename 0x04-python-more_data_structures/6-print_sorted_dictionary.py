#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    so = sorted(a_dictionary.items())
    for a, b in so:
        print("{}: {}".format(a, b))

#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
    f.closed
    return line_count

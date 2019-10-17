#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        a = 1
        if nb_lines:
            nb_lines += 1
        for line in f:
            if a == nb_lines:
                break
            print(line, end='')
            a += 1
    f.closed

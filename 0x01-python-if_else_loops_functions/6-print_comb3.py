#!/usr/bin/python3
for first in range(0, 9):
    for second in range(0, 10):
        if first == 8 and second == 9:
            break
        if first != second and first < second:
            print("{:d}{:d}".format(first, second), end=', ')
print(89)

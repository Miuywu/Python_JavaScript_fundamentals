#!/usr/bin/python3
for a in range(ord('a'), ord('a') + 26):
    if a != ord('e') and a != ord('q'):
        print("{:c}".format(a), end='')

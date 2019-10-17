#!/usr/bin/python3
def uppercase(str):
    for a in range(0, len(str)):
        shift = 0
        if ord(str[a]) >= ord('a') and ord(str[a]) <= ord('z'):
            shift = -32
        print("{:c}".format(ord(str[a]) + shift), end='')
    print()

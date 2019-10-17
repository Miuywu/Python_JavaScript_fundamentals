#!/usr/bin/python3
import sys
if __name__ == '__main__':
    ac = len(sys.argv)
    lol = 's'
    punc = ':'
    if ac is 1:
        punc = '.'
    if ac is 2:
        lol = ''
    print("{:d} argument{:s}{:s}".format(ac - 1, lol, punc))
    if ac > 1:
        index = 0
        for arguments in sys.argv:
            if index > 0:
                print("{:d}: {:s}".format(index, arguments))
            index += 1

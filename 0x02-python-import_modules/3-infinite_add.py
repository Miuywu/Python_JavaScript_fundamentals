#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    ac = len(sys.argv)
    sum = 0
    a = 1
    while a < ac:
        sum += int(sys.argv[a])
        a += 1
    print("{}".format(sum))

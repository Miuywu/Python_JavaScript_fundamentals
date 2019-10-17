#!/usr/bin/python3
start = ord('z')
stop = ord('a') - 1
flag = 0
while start > stop:
    if flag is 1:
        print("{:c}".format(start - 32), end='')
        flag = 0
    else:
        print("{:c}".format(start), end='')
        flag = 1
    start -= 1

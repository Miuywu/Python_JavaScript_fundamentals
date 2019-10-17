#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        mod10 = -number % 10
    else:
        mod10 = number % 10
    print(mod10, end='')
    return (mod10)

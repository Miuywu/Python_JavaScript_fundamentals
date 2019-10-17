#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 15 == 0:
            out = "FizzBuzz"
        elif a % 3 == 0:
            out = "Fizz"
        elif a % 5 == 0:
            out = "Buzz"
        else:
            out = a
        print("{} ".format(out), end='')

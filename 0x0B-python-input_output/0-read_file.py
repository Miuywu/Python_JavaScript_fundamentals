#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end='')

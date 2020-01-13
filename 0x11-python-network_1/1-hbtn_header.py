#!/usr/bin/python3
""" gets certain variable from attrs in url request response """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        dict = response.info()
        print(dict.get('X-Request-Id'))

#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
        dict = response.info()
        print(dict.get('X-Request-Id'))

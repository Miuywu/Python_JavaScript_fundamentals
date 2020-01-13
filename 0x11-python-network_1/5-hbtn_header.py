#!/usr/bin/python3
""" uses requests package to request url """
import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-ID'))

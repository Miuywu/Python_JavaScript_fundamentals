#!/usr/bin/python3
""" tries to get a url response, if error catches and prints """
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)

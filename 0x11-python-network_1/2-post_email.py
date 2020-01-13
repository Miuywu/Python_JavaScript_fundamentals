#!/usr/bin/python3
""" encodes dict entry into urlencoded data """
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    encoded = urllib.parse.urlencode({'email': sys.argv[2]})
    asci = encoded.encode('ascii')
    request_values = urllib.request.Request(sys.argv[1], asci)
    with urllib.request.urlopen(request_values) as response:
        html = response.read()
        print(html.decode('UTF-8'))

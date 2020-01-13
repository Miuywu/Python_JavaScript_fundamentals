#!/usr/bin/python3
""" encodes dict entry into urlencoded data """
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    encoded = urllib.parse.urlencode({'email': sys.argv[2]})
    asci = encoded.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], post_data) as response:
        html = response.read()
        print(html.decode('UTF-8'))

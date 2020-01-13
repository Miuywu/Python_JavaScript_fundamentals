#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    u8 = html.decode('utf-8')
    print("\t- utf8 content: {}".format(u8))

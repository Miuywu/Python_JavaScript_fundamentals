#!/usr/bin/python3
""" Rise of the skywalker was meh """
import sys
import requests


if __name__ == "__main__":
    c = sys.argv[1]
    try:
        resp = requests.get('https://swapi.co/api/people/?search={}'.format(c))
        derulo = resp.json()
        if derulo:
            print('Number of results:', derulo['count'])
            for jason in derulo.get('results'):
                print(jason.get('name'))
        else:
            print('No result')
    except:
        print('Not a valid JSON')

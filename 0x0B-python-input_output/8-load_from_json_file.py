#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename) as f:
        obj = json.load(f)
        return obj

#!/usr/bin/python3
import sys
jason_derulo = __import__('8-load_from_json_file').load_from_json_file
jason_momoa = __import__('7-save_to_json_file').save_to_json_file

try:
    the_list = jason_derulo('add_item.json')
except:
    the_list = []

for a in range(1, len(sys.argv)):
    the_list.append(sys.argv[a])

jason_momoa(the_list, 'add_item.json')

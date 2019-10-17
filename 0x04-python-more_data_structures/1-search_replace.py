#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for a in range(0, len(my_list)):
        x = my_list[a]
        if x is search:
            x = replace
        new.append(x)
    return new

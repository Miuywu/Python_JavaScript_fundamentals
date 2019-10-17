#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        largest = my_list[0]
        for a in range(len(my_list)):
            if largest < my_list[a]:
                largest = my_list[a]
        return largest
    else:
        return None

#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return
    curr = len(list_of_integers) // 2
    fin = 0
    while fin == 0:
        if curr == 0 and list_of_integers[curr + 1] < list_of_integers[curr]:
            return list_of_integers[curr]
        elif curr == len(list_of_integers) - 1 and list_of_integers[curr - 1] < list_of_integers[curr]:
            return list_of_integers[curr]
        elif list_of_integers[curr - 1] < list_of_integers[curr] and list_of_integers[curr + 1] < list_of_integers[curr]:
            return list_of_integers[curr]
        elif list_of_integers[curr + 1] and list_of_integers[curr + 1] > list_of_integers[curr]:
            curr += 1
            if curr == list_of_integers:
                return None
        elif list_of_integers[curr - 1] and list_of_integers[curr - 1] > list_of_integers[curr]:
            curr -= 1
            if curr == -1:
                return None
        else:
            fin = 1

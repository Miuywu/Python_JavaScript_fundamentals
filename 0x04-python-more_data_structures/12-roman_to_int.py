#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    count = 0
    dec = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for a in range(0, len(roman_string)):
        if roman_string[a] in dic.keys():
            for key in dic:
                if key is roman_string[a]:
                    if a != len(roman_string) - 1:
                        if dic[key] < dic[roman_string[a + 1]]:
                            dec -= dic[key]
                        else:
                            dec += dic[key]
                    else:
                        dec += dic[key]
        count += 1
    return dec

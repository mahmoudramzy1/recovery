#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        if (len(roman_string) == 1):
            return d[roman_string]
        n = 0
        y = 0
        for i in range(1, len(roman_string)):
            y = d[roman_string[i]]
            x = d[roman_string[i - 1]]
            if i == (len(roman_string)-1):
                n += y
            if x >= y:
                n += x
            else:
                n -= x
        return n
    return 0

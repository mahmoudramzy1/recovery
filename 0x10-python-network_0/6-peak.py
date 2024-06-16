#!/usr/bin/python3
"""get the peak element"""


def find_peak(list_of_integers):
    """find peak element in the list"""
    for i in list_of_integers:
        x = list_of_integers.index(i)
        p = 0
        ne = 0

        if len(set(list_of_integers)) == 1:
            return list_of_integers[0]

        if x > 0:
            if list_of_integers[x - 1] < list_of_integers[x]:
                p = i
        if x < (len(list_of_integers) - 1):
            if list_of_integers[x + 1] < list_of_integers[x]:
                ne = i
        if x == 0 and ne != 0:
            return ne
        if x == (len(list_of_integers) - 1) and p != 0:
            return p
        if p == ne and p != 0:
            return p

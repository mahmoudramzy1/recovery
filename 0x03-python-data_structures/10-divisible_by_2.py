#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    m = 0
    new = list(my_list)
    for i in my_list:
        if i % 2 == 0:
            new[m] = True
            m += 1
        else:
            new[m] = False
            m += 1
    return new

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = []
    for i in my_list:
        if i == search:
            n.append(replace)
        else:
            n.append(i)
    return n

#!/usr/bin/python3
for i in range(0, 10, 1):
    for n in range(0, 10, 1):
        if (i != n and i < n):
            print("{:d}{:d}".format(i, n), end="\n" if i == 8 else ", ")

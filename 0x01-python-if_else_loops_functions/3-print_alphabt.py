#!/usr/bin/python3

a = ord('a')

while a <= 122:
    if a == 101 or a == 113:
        a += 1
        continue
    print("{:c}".format(a), end="")
    a += 1

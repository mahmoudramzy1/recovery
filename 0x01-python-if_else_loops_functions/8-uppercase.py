#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        n = ord(c)
        if n in range(97, 123):
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    i = len(args)
    result = 0
    if i == 0:
        print("0")
    else:
        for n in range(i):
            result += int(args[n])
        print(result)

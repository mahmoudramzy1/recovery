#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    i = len(args)
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:\n{}: {}".format(i, args[0]))
    else:
        print("{} arguments:".format(i))
        for n in range(1, i + 1):
            print("{}: {}".format(n, args[n - 1]))

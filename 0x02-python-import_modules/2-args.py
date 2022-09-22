#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argL = len(argv)
    print("{:d} {:s}{:s}".format(argL - 1, "argument" if argL <= 2 else "arguments", 
    "." if argL == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))

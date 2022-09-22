#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    al = len(argv)
    print("{:d} {:s}{:s}".format(al - 1,
                                 "argument" if al <= 2 else "arguments",
                                 "." if al == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argL = []
    for i, s in enumerate(argv):
        if i > 0:
            argL.append(int(s))
    print(sum(argL))

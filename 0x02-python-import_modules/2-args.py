#!/usr/bin/python3

import sys

argc = len(sys.argv)

if __name__ == "__main__":
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))

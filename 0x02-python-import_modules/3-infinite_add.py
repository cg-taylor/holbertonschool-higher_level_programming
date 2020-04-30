#!/usr/bin/python3

import sys

argc = len(sys.argv) - 1
sum = 0

if __name__ == "__main__":
    for i in range(1, argc):
        sum = sum + int(sys.argv[argc])
    print(sum)

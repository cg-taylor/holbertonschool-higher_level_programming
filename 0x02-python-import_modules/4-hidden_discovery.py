#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    for i in range(0, len(names)):
        if ord('a') <= ord(str(names[i][0])) <= ord('z'):
            print(str(names[i]))

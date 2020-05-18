#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        while idx < x:
            print("{:d}".format(my_list[idx]),
                  end="\n" if idx is x - 1 else "")
            idx = idx + 1
        return x
    except IndexError:
        print("")
        return idx

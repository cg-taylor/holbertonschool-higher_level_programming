#!/usr/bin/python3


def add_tuple(tuple_a, tuple_b):
    sum1, sum2 = 0, 0
    size_a = len(tuple_a)
    size_b = len(tuple_b)

    if size_a >= 1:
        sum1 += tuple_a[0]
    if size_a >= 2:
        sum2 += tuple_a[1]

    if size_b >= 1:
        sum1 += tuple_b[0]
    if size_b >= 2:
        sum2 += tuple_b[1]

    new_tuple = sum1, sum2
    return new_tuple

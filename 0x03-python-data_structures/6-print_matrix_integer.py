#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()

    for row in matrix:
        for idx in range(len(row)):
            print("{:d}".format(row[idx]),
                  end="\n" if idx is len(row) - 1 else " ")

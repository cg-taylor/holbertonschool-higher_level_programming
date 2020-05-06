#!/usr/bin/bash


def multiple_returns(sentence):
    length = 0
    first_ch = ""

    if not sentence:
        return 0, None
    else:
        first_ch += sentence[0]

    length = len(sentence)

    return length, first_ch

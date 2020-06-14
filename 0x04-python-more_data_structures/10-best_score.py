#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    best_name = None
    for name, score in a_dictionary.items():
        if score > best:
            best = score
            best_name = name
    return best_name

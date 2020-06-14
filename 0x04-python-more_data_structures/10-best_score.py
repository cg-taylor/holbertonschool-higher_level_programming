#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return None
    best = 0
    for name in a_dictionary.keys():
        if a_dictionary[name] > best:
            best = a_dictionary[name]
            star = name
    return star

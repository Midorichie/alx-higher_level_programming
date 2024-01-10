#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for m, n in tmp.items():
        if value == n:
            a_dictionary.pop(m)
    return a_dictionary

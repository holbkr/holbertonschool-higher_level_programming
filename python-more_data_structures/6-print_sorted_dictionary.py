#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.keys())
    sk = sorted(k)

    for k in sk:
        print(f"{k}: {a_dictionary[k]}")

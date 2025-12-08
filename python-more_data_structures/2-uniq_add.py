#!/usr/bin/python3

def uniq_add(my_list=[]):
    s = 0
    for i in set(my_list):
        s += i
    return s

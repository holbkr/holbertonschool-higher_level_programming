#!/usr/bin/python3

'''
4-from_json_string.py
Module that add a function who return an object from a JSON string
'''
import json


def from_json_string(my_str):
    '''Function that returns an object (Python data structure)
    represented by a JSON string:'''
    convert_obj = json.loads(my_str)
    return convert_obj

#!/usr/bin/python3

'''
8-class_to_json.py
Module that add a function who returns the dictionary description of an object
'''


def class_to_json(obj):
    '''Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object'''
    new_dict = obj.__dict__
    return new_dict

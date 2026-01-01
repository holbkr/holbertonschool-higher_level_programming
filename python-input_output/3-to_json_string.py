#!/usr/bin/python3
'''
3-to_json_string.py
Module that add a function who convert a python object to a json format
'''
import json


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object'''
    json_convertion = json.dumps(my_obj, ensure_ascii=False)
    return json_convertion

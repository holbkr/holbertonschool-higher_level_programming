#!/usr/bin/python3

'''
5-save_to_json_file.py
Module that add a function who writes an Object to a text file, using a JSON
representation'''
import json


def save_to_json_file(my_obj, filename):
    '''Function that writes an object to a test file using JSON'''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)

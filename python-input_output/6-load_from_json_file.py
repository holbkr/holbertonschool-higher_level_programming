#!/usr/bin/python3

'''6-load_from_json_file.py
Module who add a function that creates an Object from a “JSON file”'''
import json


def load_from_json_file(filename):
    '''function that create an object from a JSON File'''
    with open(filename, "r", encoding="utf-8") as file_json:
        new_obj = json.load(file_json)
        return new_obj

#!/usr/bin/python3
'''
task_00_basic_serialization.py
Serialize and deserialized python object from/to json file
'''
import json


def serialize_and_save_to_file(data, filename):
    '''Serialize a python object to a json file'''
    # Your code here to serialize and save data to the specified file
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def load_and_deserialize(filename):
    '''Deserialize a json file into a python object'''
    # Your code here to load and deserialize data from the specified file
    with open(filename, "r", encoding="utf-8") as json_file:
        data_deserialized = json.load(json_file)
    return data_deserialized

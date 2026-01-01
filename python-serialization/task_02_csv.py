#!/usr/bin/python3
'''
task_02_csv.py
File that add a function who convert a csv file into a json file
'''
import csv
import json


def convert_csv_to_json(csv_file):
    '''Function that convert the CSV file in argument into a json file named
    data.json return True if the function succeed, False if not'''
    try:
        with open(csv_file, "r", newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            with open("data.json", "w", encoding="utf-8") as json_file:
                dictlist = []
                for row in csv_data:
                    dictlist.append(row)
                json.dump(dictlist, json_file, ensure_ascii=False)
        return True
    except (FileNotFoundError, TypeError, EOFError, ImportError):
        return False

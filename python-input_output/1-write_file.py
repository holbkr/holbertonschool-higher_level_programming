#!/usr/bin/python3
'''
1-write_file.py
module that add a function who write in a file
'''


def write_file(filename="", text=""):
    '''function that overwrite a file or create a new file if the file doesn't
    exist with the text wanted'''
    with open(filename, "w", encoding='utf-8') as file:
        count = file.write(text)
    return count

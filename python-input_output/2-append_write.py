#!/usr/bin/python3
'''2-append_write.py
Module that add a function that add text at the end of a file'''


def append_write(filename="", text=""):
    '''Function that add a text at the end of a file, if the file is not found
    create a new one'''
    with open(filename, "a", encoding='utf-8') as file:
        count = file.write(text)
        return count

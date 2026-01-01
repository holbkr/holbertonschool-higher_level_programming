#!/usr/bin/python3

'''
9-student/py
Module that add the class student with all its attributes and methods
'''


class Student:
    '''Creating a class Student with all its attributes and methods'''

    def __init__(self, first_name, last_name, age):
        '''Initialization of the instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Adding a method that retrieve the dictionnary format of all
        the attributes of the instance'''
        new_dict = self.__dict__
        return new_dict

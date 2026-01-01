#!/usr/bin/python3

'''
11-student/py
Module that add the class student with all its attributes and methods
'''


class Student:
    '''Creating a class Student with all its attributes and methods'''

    def __init__(self, first_name, last_name, age):
        '''Initialization of the instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Adding a method that retrieve the dictionnary format of all
        the attributes of the instance or of the specified attributes'''
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict.update({i: getattr(self, i)})
            return new_dict

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]

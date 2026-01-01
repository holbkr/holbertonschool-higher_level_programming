#!/usr/bin/python3
'''
task_01_pickle.py
Module that add a class CustomObject with its methods and attributes
'''
import pickle


class CustomObject:
    '''Creation of the class CustomObject who initialize instances with the
    name, age and student status'''
    def __init__(self, name, age, is_student):
        '''initialization of the instance'''
        if type(name) is str:
            self.name = name
        if type(age) is int:
            self.age = age
        if type(is_student) is bool:
            self.is_student = is_student

    @classmethod
    def deserialize(cls, filename):
        '''serialize the instance'''
        try:
            with open(filename, "rb") as pickle_file:
                data = pickle.load(pickle_file)
                return data
        except (FileNotFoundError, EOFError, ImportError):
            return None

    def display(self):
        '''print the attributes of the instance'''
        print(f"Name: {self.name}\nAge: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''deserialize the instance'''
        try:
            with open(filename, "wb") as pickle_file:
                pickle.dump(self, pickle_file)
        except (FileNotFoundError, TypeError):
            return None

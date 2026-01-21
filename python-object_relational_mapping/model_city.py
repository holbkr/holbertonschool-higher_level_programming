#!/usr/bin/python3
"""model_city.py
Creation of the class city for SQLAlchemy in order to use ORM"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''Class that represents the table city in a database'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

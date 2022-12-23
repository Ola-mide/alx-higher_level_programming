#!usr/bin/python3
"""
A module that contains a City class and an instance Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    A class that links to a table and creates columns using class attributes

    Attr:
        id (int): column for id
        name (str): column for state names
        state_id (int): column for state id
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False
            )
    name = Column(
            String(128),
            nullable=False
            )
    state_id = Column(
            Integer,
            ForeignKey('state.id')
            )

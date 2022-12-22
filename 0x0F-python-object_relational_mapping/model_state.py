#!usr/bin/python3
"""
A module that contains a State class and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    A class that links to a table and creates columns using class attributes

    Attr:
        id (int): column for id
        name (str): column for state names
    """

    __tablename__ = 'states'
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

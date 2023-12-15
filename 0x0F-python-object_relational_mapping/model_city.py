#!/usr/bin/python3
"""
Script defines a City Class
to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declaarative_base

Base = declarative_base()

class City(Base):
    """City class

    Attributes:
        __tablename (str): The table name of class
        id (int): The id of the class
        name (str): The name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

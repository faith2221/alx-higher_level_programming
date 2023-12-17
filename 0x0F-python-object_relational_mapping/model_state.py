#!/usr/bin/python3
"""
Script defines a State Class and a Base Class
to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sate(Base):
    """State class

    Attributes:
        __tablename (str): The table name of class
        id (int): The State id of the class
        name (str): The state name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

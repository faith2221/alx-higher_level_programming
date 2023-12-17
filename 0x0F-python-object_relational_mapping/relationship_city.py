#!/usr/bin/python3
"""
Script defines a City Class
to work with MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename (str): The table name of class
        id (int): The id of the class
        name (str): The name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

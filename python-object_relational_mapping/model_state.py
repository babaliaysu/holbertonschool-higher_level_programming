#!/usr/bin/python3
"""
Definition of the State class and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base obyektini yaradırıq
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
Contains class definition of State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

from sqlalchemy import create_engine
engine = create_engine('mysql://kathy2470:kathylenemukisa@localhost:3306/hbtn_0e_6_usa')
Base.metadata.create_all(engine)

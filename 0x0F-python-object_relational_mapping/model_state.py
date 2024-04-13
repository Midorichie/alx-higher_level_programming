#!/usr/bin/python3
"""model_state module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
import sys


Base = declarative_base()


class State(Base):
    '''
    contains the class definition of a state and
    an instance Base = declarative_base()
    '''
    __tablename__ = "states"
    id = column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement=True
            )
    name = column(String(128), nullable=False)

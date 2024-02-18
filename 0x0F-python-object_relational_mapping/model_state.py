#!/usr/bin/python3
"""
First Use of ORM
creating engine => creating Mapping of table => Bind to database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):

    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

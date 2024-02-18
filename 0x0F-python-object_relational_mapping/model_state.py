#!/usr/bin/python3
"""
First Use of ORM
creating engine => creating Mapping of table => Bind to database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


user = sys.argv[1]
pswd = sys.argv[2]
db = sys.argv[3]

"""first step creating engine"""

eng_url = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pswd, db)
engine = create_engine(eng_url)

"""seconed step creating model map"""

Base = declarative_base()


class State(Base):

    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)

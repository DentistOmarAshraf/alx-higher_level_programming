#!/usr/bin/python3
"""
Fetch all Data in Model
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


usr = sys.argv[1]
pd = sys.argv[2]
db = sys.argv[3]

eng_url = f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}"
engine = create_engine(eng_url, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()


for obj in session.query(State).all():
    print(f"{obj.id}: {obj.name}")

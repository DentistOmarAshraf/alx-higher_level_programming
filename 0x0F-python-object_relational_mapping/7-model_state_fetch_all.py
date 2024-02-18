#!/usr/bin/python3
"""
Fetch all Data in Model
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""Usr and password and database"""
if __name__ == "__main__":
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]

    eng_url = f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}"
    engine = create_engine(eng_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    """SELECT id, name FROM states ORDER BY id"""
    for obj in session.query(State).order_by(State.id).all():
        print(f"{obj.id}: {obj.name}")
    session.close()

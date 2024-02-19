#!/usr/bin/python3
"""
Join Tables
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, join

if __name__ == "__main__":
    """Create Engine"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)

    """Session Start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    qr = session.query(State, City).join(City, State.id == City.state_id)

    for state, city in qr:
        print("{}: ({}) {}".format(state.name, state.id, city.name))

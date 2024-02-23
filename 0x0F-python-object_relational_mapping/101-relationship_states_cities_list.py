#!/usr/bin/python3
"""
print list from relateion on-to-many
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """Engine Start"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")

    """Session Start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for ci in state.cities:
            print(f"    {ci.id}: {ci.name}")

    session.close()

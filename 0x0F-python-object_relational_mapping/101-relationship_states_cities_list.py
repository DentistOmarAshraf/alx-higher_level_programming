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
    """Loading tables"""
    Base.metadata.create_all(engine)

    """Session Start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    state_list = session.query(State, City).join(
                 City, State.id == City.state_id).order_by(
                 State.id, City.id)

    nametemp = ""
    for state, city in state_list:
        if state.name != nametemp:
            print(f"{state.id}: {state.name}")
            nametemp = state.name
        print(f"\t{city.id}:{city.name}")

    session.close()

#!/usr/bin/python3
"""
print list from relateion on-to-many
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    """Engine Start"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}",
                           pool_pre_ping=True)

    """Session Start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    stname = ""
    for ci in session.query(City).order_by(City.id):
        if ci.state.name != stname:
            print(f"{ci.state.id}: {ci.state.name}")
            for ci in ci.state.cities:
                print(f"    {ci.id}: {ci.name}")
        stname = ci.state.name

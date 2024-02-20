#!/usr/bin/python3
"""
Relationship task
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Start Engine"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)

    """Session Start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """create state and city"""
    st = State(name="California")
    ci = City(name="San Francisco", state_id=st.id, state=st)
    st.cities = [ci]
    session.add(st)
    session.add(ci)
    session.commit()
    session.close()

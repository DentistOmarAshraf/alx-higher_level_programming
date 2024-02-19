#!/usr/bin/python3
"""
Fetching Data
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """creating Engine"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)

    """Session start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """start to search"""
    search = sys.argv[4]

    try:
        obj = session.query(State).filter(State.name.like(search)).one()
        print(obj.id)
    except Exception:
        print("Not found")

    session.close()

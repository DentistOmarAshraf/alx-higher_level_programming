#!/usr/bin/python3
"""
Fetch First state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    creating Engine
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Using query.filter to fetch first state"""

    first = session.query(State).first()

    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()

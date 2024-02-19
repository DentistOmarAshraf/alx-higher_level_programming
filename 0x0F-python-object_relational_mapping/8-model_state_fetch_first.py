#!/usr/bin/python3
"""
Fetch First state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """creating Engine"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Using query.filter to fetch first state"""

    all_obj = session.query(State).filter(State.id == '1').all()

    if (len(all_obj) == 0):
        print("Nothing")
    else:
        for obj in all_obj:
            print(f"{obj.id}: {obj.name}")

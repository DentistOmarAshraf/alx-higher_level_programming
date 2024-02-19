#!/usr/bin/python3
"""
Fetching from table
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    """creating Engine"""
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")
    """creating tables from model inherit from Base"""
    Base.metadata.create_all(engine)
    
    """Start Session to start query"""
    Session = sessionmaker(bind=engine)
    session = Session()

    obj_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    if obj_a:
        for row in obj_a:
            print(f"{row.id}: {row.name}")
    else:
        print("Nothing")


    session.close()

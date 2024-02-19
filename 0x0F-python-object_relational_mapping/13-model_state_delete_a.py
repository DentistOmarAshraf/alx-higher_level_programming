#!/usr/bin/python3
"""
Delete from table
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Create Engine"""
    usr = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pd}@localhost:3306/{db}")
    Base.metadata.create_all(engine)

    """Session start"""
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(State).filter(State.name.like("%a%"))
    obj.delete()

    session.commit()
    session.close()

#!/usr/bin/python3
"""
Adding To Table
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
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

    """Adding to table"""
    session.add(State(name="Louisiana"))
    session.commit()

    last = session.query(State).order_by(State.id.desc()).first()
    print(last.id)
    session.close()

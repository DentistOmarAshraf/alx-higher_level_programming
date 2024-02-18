#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    usr = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]

    eng_url = f"mysql+mysqldb://{usr}:{pswd}@localhost:3306/{db}"
    engine = create_engine(eng_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

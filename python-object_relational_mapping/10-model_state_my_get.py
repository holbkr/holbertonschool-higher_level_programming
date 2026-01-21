#!/usr/bin/python3
"""Module that create a session and request the state id and name
from the table State that correspond to the name of the state passed in
argument"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]

    state = session.query(State).filter(
        State.name.like(f"{state_name}")).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

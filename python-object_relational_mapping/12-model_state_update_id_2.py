#!/usr/bin/python3
"""Module that create a session and changed the name of the state
with an id = 2, to New Mexico """

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

    state = session.query(State).filter(
        State.id.like(2)).first()

    state.name = "New Mexico"
    session.commit()
    session.close()

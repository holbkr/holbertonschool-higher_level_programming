#!/usr/bin/python3
"""Module that create a session and delete from the table the states
that contains the letter 'a' """

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

    all_states = session.query(State).order_by(
        State.id).filter(State.name.like('%a%')).all()

    for row in all_states:
        session.delete(row)
    session.commit()
    session.close()

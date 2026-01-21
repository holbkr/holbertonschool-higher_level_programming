#!/usr/bin/python3
"""Module that create a session and request all the cities and their
informationsfrom the table City"""

import sys
from model_state import Base, State
from model_city import City
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

    all_cities = session.query(State.name, City.id, City.name).join(
        City, City.state_id == State.id).order_by(
        State.id).all()

    for row in all_cities:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    session.close()

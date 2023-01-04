#!/usr/bin/python3
"""
A module that lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
                print("{}: {}".format(
                    state.id,
                    state.name
                    ))
                for city in state.cities:
                    print("\t{}: {}".format(
                        city.id,
                        city.name
                        ))

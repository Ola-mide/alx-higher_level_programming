#!/usr/bin/python3
"""
A module that inserts data into the tables of the database hbtn_0e_100_usa
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

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)

    session.commit()
    session.close()

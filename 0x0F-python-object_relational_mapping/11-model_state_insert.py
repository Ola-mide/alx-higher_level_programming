#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
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

    new_State = State(name="Louisiana")
    session.add(new_State)
    session.commit()

    state = session.query(State).filter_by(name="Louisiana").first()
    if state:
        print(state.id)
    session.close()

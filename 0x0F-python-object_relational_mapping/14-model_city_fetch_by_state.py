#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """prints"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    c = session.query(City, State).filter(City.state_id == State.id)
    for entry in c:
        print("{}: ({}) {}".format(entry.State.name, entry.City.id, entry.City.name))
    session.close()

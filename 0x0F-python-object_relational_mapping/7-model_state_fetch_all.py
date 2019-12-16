#!/usr/bin/python3
import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

""" script that lists all State objects from the database hbtn_0e_6_usa """

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    session.close()

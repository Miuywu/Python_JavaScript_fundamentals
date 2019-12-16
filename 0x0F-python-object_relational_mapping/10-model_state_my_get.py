#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ if comment """

    engine = create_engine("mysql+mysqldb://" +
                           "{}:{}@localhost/{}".format(sys.argv[1],
                                                       sys.argv[2],
                                                       sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a = 0
    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print(state.id)
            a = 1
    if a == 0:
        print("Not found")
    session.close()

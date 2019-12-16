#!/usr/bin/python3
""" module contains the class state and instance base """
from model_state import Base, State
from sqlalchemy import Column, Integer, String


class City(Base):
    """ state """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)

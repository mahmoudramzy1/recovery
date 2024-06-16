#!/usr/bin/python3

"""first use to sqlalqemy"""

from sqlalchemy import Integer, String, create_engine, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """state class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""fetch all states"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ = '__main__':
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                                    .format(sys.argv[1], 
                                    sys.argv[2],
                                    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all = (engine)
    session = sessionmaker(bind=engine)
    Session = session()

    for state in Session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    Session.close()

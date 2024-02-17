#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(
            State.id, City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("     {}: {}".format(city.id, city.name))

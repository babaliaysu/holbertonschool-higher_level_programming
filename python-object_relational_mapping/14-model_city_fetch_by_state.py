#!/usr/bin/python3
""" Lists all City objects from the database hbtn_0e_14_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # City və State obyektlərini join edərək çəkirik
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Nəticələri tələb olunan formatda çap edirik
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

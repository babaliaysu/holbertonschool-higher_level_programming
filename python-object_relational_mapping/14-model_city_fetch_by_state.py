#!/usr/bin/python3
"""
Script to list all cities from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Giriş arqumentlərini al
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Mühərriki yarat
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    # Sessiya yarat
    Session = sessionmaker(bind=engine)
    session = Session()

    # Məlumatları al (City və State-i join edərək)
    # Sıralama cities.id üzrə aparılır
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Nəticələri çap et
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Sessiyanı bağla
    session.close()

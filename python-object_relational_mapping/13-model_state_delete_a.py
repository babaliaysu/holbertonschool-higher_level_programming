#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Verilənlər bazasına qoşulma
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # 2. Sessiya yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Adında 'a' hərfi olan obyektləri tapıb silirik
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    # 4. Dəyişikliyi bazaya tətbiq edirik
    session.commit()

    # 5. Sessiyanın bağlanması
    session.close()

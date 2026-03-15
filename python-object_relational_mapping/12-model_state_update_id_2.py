#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
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

    # 3. İd-si 2 olan ştatı tapırıq
    state_to_update = session.query(State).filter(State.id == 2).first()

    # 4. Əgər ştat tapılıbsa, adını dəyişirik
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # 5. Sessiyanın bağlanması
    session.close()

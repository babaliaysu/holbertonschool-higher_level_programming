#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # 1. Engine yaradırıq (bazaya qoşulma nöqtəsi)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # 2. Sessiya yaradırıq
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Ştatları id-yə görə sıralanmış şəkildə çəkirik
    states = session.query(State).order_by(State.id).all()

    # 4. Nəticələri çap edirik
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 5. Sessiyanı bağlayırıq
    session.close()

#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Engine və Session-un düzgün qurulması
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Silinəcək obyektləri tapırıq
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Obyektləri dövr ilə silirik
    for state in states:
        session.delete(state)

    # Tranzaksiyanı bağlayırıq (və dəyişikliyi bazaya yazırıq)
    session.commit()
    session.close()

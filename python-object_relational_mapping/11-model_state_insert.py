#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # 3. Yeni State obyektinin yaradılması
    new_state = State(name="Louisiana")

    # 4. Obyektin sessiyaya əlavə edilməsi və commit olunması
    session.add(new_state)
    session.commit()

    # 5. Yeni generasiya edilmiş id-ni çap edirik
    print(new_state.id)

    # 6. Sessiyanın bağlanması
    session.close()

#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Sessiya yaradılması
    Session = sessionmaker(bind=engine)
    session = Session()

    # Verilmiş ada uyğun ştatı axtarırıq
    # Təhlükəsizlik üçün filter istifadə edirik
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Nəticəni yoxlayıb çap edirik
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

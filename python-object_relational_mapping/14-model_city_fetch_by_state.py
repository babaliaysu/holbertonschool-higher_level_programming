#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create the engine to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create a configured session class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City and State objects using a JOIN, ordered by City id
    results = session.query(State, City).join(City).order_by(City.id).all()

    # Iterate through the results and print in the specified format
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()

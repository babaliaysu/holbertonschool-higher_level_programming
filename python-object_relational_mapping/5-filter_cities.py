#!/usr/bin/python3
""" Lists all cities of a given state from the database hbtn_0e_4_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # JOIN və parametrləşdirilmiş sorğu istifadə edirik
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    # Nəticələri vergüllə ayıraraq çap edirik
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()

#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Komanda sətri arqumentlərini alırıq
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # MySQL serverinə qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Cursor yaradırıq
    cursor = db.cursor()

    # Parametrləşdirilmiş sorğu istifadə edirik (SQL Injection qarşısını alır)
    # MySQLdb-də %s yerinə qoyulan dəyərlər avtomatik kotirovka olunur
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, ('N%',))

    # Nəticələri alırıq və çap edirik
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()

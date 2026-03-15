#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
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

    # Sorğuları icra etmək üçün cursor yaradırıq
    cursor = db.cursor()

    # Məlumatları çəkirik
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələri alırıq
    rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()

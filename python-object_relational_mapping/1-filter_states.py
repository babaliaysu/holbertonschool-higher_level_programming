#!/usr/bin/python3
""" Script that lists all states with a name starting with N """
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

    # Məlumatları süzgəcdən keçiririk
    # 'N%' - adı N hərfi ilə başlayan bütün sətirləri tapır
    # BINARY açar sözü 'N' hərfini böyük-kiçik hərfə həssas (case-sensitive) edir
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Nəticələri alırıq
    rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()

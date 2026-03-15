#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument,
using a safe approach against MySQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    # SQL injection-dan qorunmaq üçün '%s' yer tutucusundan istifadə edirik
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

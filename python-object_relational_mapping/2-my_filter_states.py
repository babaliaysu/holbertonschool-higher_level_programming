#!/usr/bin/python3
""" Script that takes an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument securely. """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Use parameterized query to prevent SQL Injection
    # The %s is a placeholder for the database driver, not string formatting
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and display all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()

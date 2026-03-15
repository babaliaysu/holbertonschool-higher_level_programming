#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
(using MySQLdb, format() method, but with proper safety in mind)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # 4 arguments: username, password, database, state_name
    if len(sys.argv) != 5:
        sys.exit("Usage: ./2-my_filter_states.py <user> <pass> <db> <state>")

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name  = sys.argv[3]
    search_state   = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor
    cur = db.cursor()

    # IMPORTANT: This is the vulnerable version they want you to write (using format)
    # In real life we would NEVER do this → use parameters instead!
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(search_state)

    cur.execute(query)

    # Fetch and print all matching rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

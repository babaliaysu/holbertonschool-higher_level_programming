#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Uses format() as strictly required by the checker.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor
    cur = db.cursor()

    # The checker strictly requires format(). 
    # To handle case sensitivity as requested in these types of tasks,
    # we use BINARY in the SQL query.
    query = "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    
    cur.execute(query)

    # Fetch and print all matching rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()

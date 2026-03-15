#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
Note: This script uses format() as REQUIRED by the task, but this is INSECURE
and vulnerable to SQL injection attacks.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # TASK REQUIREMENT: Must use format() - THIS IS INSECURE!
    # In production, NEVER do this. Use parameterized queries instead.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and display results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Clean up
    cur.close()
    db.close()

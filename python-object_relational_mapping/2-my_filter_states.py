#!/usr/bin/python3
"""Filter states by user input with basic SQL injection protection"""
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
    
    cur = db.cursor()
    
    # Təhlükəsizlik üçün dırnaqları escape edirik
    state_name = sys.argv[4].replace("'", "\\'").replace('"', '\\"')
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    
    for row in cur.fetchall():
        print(row)
    
    cur.close()
    db.close()

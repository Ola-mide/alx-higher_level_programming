#!/usr/bin/python3
"""
A module that lists all states from a specific database
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY states.id ASC")
    for row in cursor.fetchall():
        if row[1][0] == "N":
            print(row)
    db.close()

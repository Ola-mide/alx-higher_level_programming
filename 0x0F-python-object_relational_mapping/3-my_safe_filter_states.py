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
            port=3306
            )
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY states.id ASC")
    for row in cursor.fetchall():
        if sys.argv[4] in row:
            print("({}, \'{}\')".format(row[0], sys.argv[4]))
    db.close()

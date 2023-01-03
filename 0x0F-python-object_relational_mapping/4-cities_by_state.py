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
    c1 = "SELECT cities.id, cities.name, states.name FROM cities "
    c2 = "JOIN states WHERE cities.state_id=states.id ORDER BY cities.id ASC"
    command = c1 + c2
    cursor.execute(command)
    for row in cursor.fetchall():
        print(row)
    db.close()

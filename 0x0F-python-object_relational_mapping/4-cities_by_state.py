#!/usr/bin/python3
"""holds one function"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """lists all states from the database hbtn_0e_usa"""
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])

    curs = database.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM states,\
    cities WHERE cities.state_id = states.id")

    a = curs.fetchall()
    for row in a:
        print(row)
    curs.close()
    database.close()

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
    curs.execute("SELECT cities.name FROM states JOIN cities\
    ON states.id = cities.state_id WHERE states.name = %s", (argv[4], ))

    a = curs.fetchall()
    b = 0
    for row in a:
        if b != 0:
            print(', ', end='')
        b += 1
        print(row[0], end='')
    print()
    curs.close()
    database.close()

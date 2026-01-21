#!/usr/bin/python3
"""4-cities_by_state.py
Module that connects to a database thanks to severals arguments in the
command line such as your username, your password and the name of the
database, it also give you the list of cities with their id ans states"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

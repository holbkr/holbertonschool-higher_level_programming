#!/usr/bin/python3
"""5-filter_cities.py
Module that connects to a database thanks to severals arguments in the
command line such as your username, your password and the name of the
database, it also give you the list of all the cities related to the state
enter in argument, in a secure way"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name = %s"
                "ORDER BY cities.id ASC", (state_name,))

    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()

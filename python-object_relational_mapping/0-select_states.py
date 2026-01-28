#!/usr/bin/python3
"""0-select_states.py
Module that connects to a database thanks to severals arguments in the
command line such as your username, your password and the name of the
database, it also give you the list of states and their id
in the table 'states'"""
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
    cur.execute("SELECT id, name FROM states ORDER BY id")
    for row in cur.fetchall():
        print(f"({row[0]}, '{row[1]}')")
    cur.close()
    db.close()

#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", 3306, username, password, dbname, charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT name FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()

#!/usr/bin/python3

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]

try:
    db = MySQLdb.connect("localhost:3306", username, password, dbname)
except:
    print("Can't connect to db")
    return 0

cursor = db.cursor()
cursor.execute("SELECT name FROM states")
results = cursor.fetchall()

print(results)

db.close()

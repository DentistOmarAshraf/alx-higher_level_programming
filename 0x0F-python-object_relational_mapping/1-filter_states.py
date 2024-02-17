#!/usr/bin/python3
"""
Connection to SQL with MySQLdb
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """establish connection with SQL"""
    conn = MySQLdb.connect(user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3],
                           port=3306,
                           host="localhost",
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE id>=4 ORDER BY id ASC")
    q_row = cur.fetchall()

    for row in q_row:
        print(row)

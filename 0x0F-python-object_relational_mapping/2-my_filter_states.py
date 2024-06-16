#!/usr/bin/python3
"""module for connect to mysql and retrive states table"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )

    mycursor = conn.cursor()

    query = """
    SELECT * FROM states WHERE name LIKE
    '{}' ORDER BY states.id ASC""".format(sys.argv[4])
    mycursor.execute(query)
    states = mycursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    mycursor.close()
    conn.close()

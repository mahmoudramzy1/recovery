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

    mycursor.execute("""SELECT cities.id, cities.name, states.name
                        FROM cities, states
                        WHERE states.id = cities.state_id
                        ORDER BY states.id ASC;""")

    states = mycursor.fetchall()
    for state in states:
        print(state)
    mycursor.close()
    conn.close()

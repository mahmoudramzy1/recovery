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

    mycursor.execute("""SELECT name FROM cities
                        WHERE cities.state_id = (
                            SELECT id FROM states WHERE states.name = %s
                        )
                        ORDER BY cities.id ASC;""", (sys.argv[4], ))

    states = mycursor.fetchall()
    cities = ", ".join(city[0] for city in states)
    print(cities)
    mycursor.close()
    conn.close()

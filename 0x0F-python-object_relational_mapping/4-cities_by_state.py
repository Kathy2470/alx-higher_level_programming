#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to the MySQL server and lists all cities in respective states.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

    Returns:
        list: List of tuples containing city information.
    """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM cities ORDER BY id")

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    cities = list_cities(username, password, database)

    for city in cities:
        print(city)

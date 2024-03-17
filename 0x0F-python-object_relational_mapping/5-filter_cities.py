#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """
    Connects to the MySQL server and lists all cities of the given state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state_name (str): Name of the state.

    Returns:
        list: List of tuples containing city information.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        # Execute query to select cities of the given state
        query = "SELECT cities.id, cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id"
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        db.close()

        return results
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    cities_by_state = list_cities_by_state(username, password, database, state_name)

    for city in cities_by_state:
        print(city)

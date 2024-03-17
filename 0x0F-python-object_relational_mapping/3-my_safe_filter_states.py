#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa where name matches the provided argument.
"""

import MySQLdb
import sys

def search_states(username, password, database, state_name):
    """
    Connects to the MySQL server and searches for states with the provided name in the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state_name (str): Name of the state to search for.

    Returns:
        list: List of tuples containing state information.
    """
    try:
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

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

    states = search_states(username, password, database, state_name)

    for row in states:
        print(row)

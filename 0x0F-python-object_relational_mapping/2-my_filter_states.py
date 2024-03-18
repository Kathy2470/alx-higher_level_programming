#!/usr/bin/python3
"""
Script to filter states safely using MySQLdb.
"""

import MySQLdb
import sys


def safe_filter_states(username, password, database, state_name):
    """
    Filter states safely using MySQLdb.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state_name (str): Name of the state to filter.

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

        cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id",
                       (state_name,))
        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results
    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    states = safe_filter_states(username, password, database, state_name)

    for row in states:
        print(row)

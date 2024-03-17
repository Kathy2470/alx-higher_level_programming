#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def get_states(username, password, database):
    """
    Connects to the MySQL server and retrieves all states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

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

        cursor.execute("SELECT * FROM states ORDER BY id")

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

    states = get_states(username, password, database)

    for row in states:
        print(row)

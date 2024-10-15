# Code taken from: SQLite Python: Creating a New Database
# Reference: https://www.sqlitetutorial.net/sqlite-python/creating-database/

"""This file provides a function to create a connection to an SQLite database.

The connection is established to a database file, and the SQLite version is printed.
If there is an error during the connection process, it is caught and printed.
The connection is always closed after the operation, whether successful or not.
"""

import sqlite3

def create_sqlite_database(filename):
    """Create a database connection to an SQLite database and print the SQLite version.

    This function attempts to connect to the SQLite database specified by the
    filename. If the connection is successful, the SQLite version is printed.
    If there is any error during the connection attempt, it catches the exception
    and prints the error message.

    Args:
        filename (str): The path to the SQLite database file.

    Raises:
        sqlite3.Error: If an error occurs during database connection, it is caught
        and printed to the console.
    """

    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as database_error:
        print(database_error)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sqlite_database("/database/src/movies.db")
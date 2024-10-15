"""This file tests the ability to query the `MOVIE` table in the database and
verify that the results match the expected data.
"""


import os
import sqlite3
import pytest

def test_query_table():
    """Test the query functionality for the `MOVIE` table in the database.

    This function connects to the SQLite database and executes a SQL query to
    retrieve the first 5 rows from the `MOVIE` table. It compares the actual
    result of the query to a predefined list of expected results (movie details)
    to ensure the query is functioning as expected.

    The database file is located at `/database/src/movies.db`, and the test
    verifies if the structure and content of the retrieved data match the
    predefined expected values.
    """

    db_path = os.path.join(os.path.dirname(__file__), '/database/src/movies.db')

    try:
        con = sqlite3.connect(db_path)
        curs = con.cursor()
        curs.execute("SELECT * FROM MOVIE LIMIT 5;")
        record = curs.fetchall()

        expected_results_ver = [
            (1, 1, 1, 'The Shawshank Redemption', 1994, 9.3, 142, 'Fear can hold you prisoner. Hope can set you free.',
             25000000, 28884504),
            (2, 1, 2, 'The Godfather', 1972, 9.2, 175, "An offer you can't refuse.", 6000000, 250341816),
            (3, 2, 3, 'The Dark Knight', 2008, 9, 152, 'Why So Serious?', 185000000, 1006234167),
            (4, 1, 4, 'The Godfather Part II', 1974, 9, 202, "All the power on earth can't change destiny.", 13000000,
             47961919),
            (5, 3, 5, '12 Angry Men', 1957, 9, 96, 'Life Is In Their Hands -- Death Is On Their Minds!', 350000, 955)
        ]

        assert record == expected_results_ver

    except sqlite3.Error as database_error:
        # Handle any database-related errors
        pytest.fail(f"Database error occurred: {database_error}")

    finally:
        # Ensure that the cursor and connection are closed
        if 'curs' in locals():
            curs.close()
        if 'con' in locals():
            con.close()

if __name__ == '__main__':
    pytest.main()

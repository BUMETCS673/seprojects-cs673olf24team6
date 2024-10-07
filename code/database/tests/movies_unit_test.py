import sqlite3
import pytest
import os

def test_query_table():
    db_path = os.path.join(os.path.dirname(__file__), '/app/src/movies.db')
    con = sqlite3.connect(db_path)
    curs = con.cursor()
    curs.execute("SELECT * FROM MOVIE LIMIT 5;")
    record = curs.fetchall()


    expected_results = [
        (1, 1, 1, 'The Shawshank Redemption', 1994, 9.3, 142,'Fear can hold you prisoner. Hope can set you free.', '25000000', '28884504'),
        (2, 1, 2, 'The Godfather', 1972, 9.2, 175, "An offer you can't refuse.", '6000000', '250341816'),
        (3, 2, 3, 'The Dark Knight', 2008, 9, 152, 'Why So Serious?', '185000000', '1006234167'),
        (4, 1, 4, 'The Godfather Part II', 1974, 9, 202,"All the power on earth can't change destiny.", '13000000', '47961919'),
        (5, 3, 5, '12 Angry Men', 1957, 9, 96, 'Life Is In Their Hands -- Death Is On Their Minds!','350000', '955')
    ]

    expected_results_ver2 = [
        (1, 1, 1, 'The Shawshank Redemption', 1994, 9.3, 142, 'Fear can hold you prisoner. Hope can set you free.',
         25000000, 28884504),
        (2, 1, 2, 'The Godfather', 1972, 9.2, 175, "An offer you can't refuse.", 6000000, 250341816),
        (3, 2, 3, 'The Dark Knight', 2008, 9, 152, 'Why So Serious?', 185000000, 1006234167),
        (4, 1, 4, 'The Godfather Part II', 1974, 9, 202, "All the power on earth can't change destiny.", 13000000,
         47961919),
        (5, 3, 5, '12 Angry Men', 1957, 9, 96, 'Life Is In Their Hands -- Death Is On Their Minds!', 350000, 955)
    ]

    assert record == expected_results_ver2
    curs.close()
    con.close()


if __name__ == '__main__':
    pytest.main()

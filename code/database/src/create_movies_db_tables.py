# Creating Movies database tables using the code from SQLite Tutorial as a reference.
# Reference: https://www.sqlitetutorial.net/sqlite-python/creating-tables/


import sqlite3

def create_tables():
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS DIRECTOR (
                director_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                director_name TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS WRITERS (
                writer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                writer_name TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS CAST (
                cast_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                cast_name TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS AGE_RATING (
                rating_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                rating_title VARCHAR(32) 
        );""",
        """CREATE TABLE IF NOT EXISTS GENRE (
                genre_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                genre_name TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS MOVIE (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                rating_id INTEGER,
                rank INTEGER,
                movie_title TEXT,
                release_date DATE,
                score DECIMAL(2,1),
                runtime INTEGER,
                tagline VARCHAR(255),
                budget DECIMAL(10,2),
                boxoffice DECIMAL(10.2)
        );""",
        """CREATE TABLE IF NOT EXISTS MOVIE_GENRE (
                movie_id INTEGER, 
                genre_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id)
                FOREIGN KEY(genre_id) REFERENCES GENRE(genre_id)
        );""",
        """CREATE TABLE IF NOT EXISTS MOVIE_CAST (
                movie_id INTEGER, 
                cast_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id)
                FOREIGN KEY(cast_id) REFERENCES CAST(cast_id)
        );""",
        """CREATE TABLE IF NOT EXISTS MOVIE_DIRECTOR (
                movie_id INTEGER, 
                director_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id)
                FOREIGN KEY(director_id) REFERENCES DIRECTOR(director_id)
        );""",
        """CREATE TABLE IF NOT EXISTS MOVIE_WRITERS (
                movie_id INTEGER, 
                writer_id INTEGER,
                FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id)
                FOREIGN KEY(writer_id) REFERENCES DIRECTOR(writer_id)
        );""",
        """CREATE INDEX idx_movie_genre ON MOVIE_GENRE(genre_id)
        ;""",
        """CREATE INDEX idx_movie_cast ON MOVIE_CAST(cast_id)
        ;""",
        """CREATE INDEX idx_movie_age_rating ON AGE_RATING(rating_id)
        ;"""]

    # create a database connection
    try:
        with sqlite3.connect('/app/src/movies.db') as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    create_tables()

"""This start_movies.py script runs all the files needed to
create the movies.db SQLite database, creates the tables,
and then loads the tables with data."""

exec(open("/app/src/create_movies_db.py").read()) # Creates the database

exec(open("/app/src/create_movies_db_tables.py").read()) # Creates tables

exec(open("/app/src/load_movies_db_data.py").read())

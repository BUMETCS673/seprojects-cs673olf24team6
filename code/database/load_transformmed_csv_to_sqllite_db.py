import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('movies.db')

# Load data from CSV files into DataFrames
movies_df = pd.read_csv('movies.csv')
directors_df = pd.read_csv('directors.csv')
writers_df = pd.read_csv('writers.csv')
casts_df = pd.read_csv('casts.csv')
age_ratings_df = pd.read_csv('age_ratings.csv')
genres_df = pd.read_csv('genres.csv')

# Load DataFrames into SQLite tables
movies_df.to_sql('MOVIE', conn, if_exists='append', index=False)
directors_df.to_sql('DIRECTOR', conn, if_exists='append', index=False)
writers_df.to_sql('WRITERS', conn, if_exists='append', index=False)
casts_df.to_sql('CAST', conn, if_exists='append', index=False)
age_ratings_df.to_sql('AGE_RATING', conn, if_exists='append', index=False)
genres_df.to_sql('GENRE', conn, if_exists='append', index=False)

# Close the connection
conn.close()
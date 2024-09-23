import pandas as pd
import sqlite3

# Load the dataset
df = pd.read_csv('IMDB Top 250 Movies.csv')

# Display the first few rows
print(df.head())


# Split the necessary columns into separate DataFrames

# 1. MOVIE DataFrame
movies_df = df[['rank', 'name', 'year', 'rating', 'certificate', 'run_time', 'tagline', 'budget', 'box_office']].copy()
movies_df.columns = ['rank', 'movie_title', 'release_date', 'score', 'rating_id', 'runtime', 'tagline', 'budget', 'boxoffice']
movies_df['release_date'] = pd.to_datetime(movies_df['release_date'].astype(str), format='%Y')

print(movies_df.head())



# 2. DIRECTOR DataFrame
print()
print('Directors')
directors_df = df['directors'].str.split(',', expand=True).stack().reset_index(drop=True).to_frame(name='director_name').drop_duplicates()
print(directors_df.head())

# 3. WRITERS DataFrame
print()
print('Writers')
writers_df = df['writers'].str.split(',', expand=True).stack().reset_index(drop=True).to_frame(name='writer_name').drop_duplicates()
print(writers_df.head())
# 4. CAST DataFrame
print()
print('Casts')
casts_df = df['casts'].str.split(',', expand=True).stack().reset_index(drop=True).to_frame(name='cast_name').drop_duplicates()
print(casts_df.head())

# 5. AGE_RATING DataFrame (assuming ratings are fixed, e.g., R, PG-13)
print()
print('Age Rating')
age_ratings_df = pd.DataFrame(df['certificate'].unique(), columns=['rating_title']).rename(columns={'rating_title': 'rating_title'})
print(age_ratings_df.head())

# 6. GENRE DataFrame
print()
print('Genre')
genres_df = df['genre'].str.split(',', expand=True).stack().reset_index(drop=True).to_frame(name='genre_name').drop_duplicates()
print(genres_df.head())

# Export DataFrames to CSV files
movies_df.to_csv('movies.csv', index=False)
directors_df.to_csv('directors.csv', index=False)
writers_df.to_csv('writers.csv', index=False)
casts_df.to_csv('casts.csv', index=False)
age_ratings_df.to_csv('age_ratings.csv', index=False)
genres_df.to_csv('genres.csv', index=False)




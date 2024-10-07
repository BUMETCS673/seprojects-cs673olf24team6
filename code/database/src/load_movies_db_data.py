import pandas as pd

raw_movie_data = pd.read_csv('/app/src/IMDB_Top_250_Movies.csv')

#print(raw_movie_data)

# Copying the data
data = raw_movie_data.copy()


#---------------------------------------------------
# Data for the AgeRating table
# Using the movie Rank to keep track of what Age Rating each movie had.
certificate_data = pd.DataFrame()
age_rating_data = pd.DataFrame()

certificate_data['rank'] = data['rank'].copy()
certificate_data['certificate'] = data['certificate'].copy()
age_rating_data['rating_title'] = data['certificate'].copy()

# Removing duplicates only from the ageRating_data
age_rating_data = age_rating_data.drop_duplicates()

pk_age_rating = [ i + 1 for i in range(age_rating_data.size)]

age_rating_data['rating_id'] = pk_age_rating
age_rating_data = age_rating_data[['rating_id','rating_title']]

certificate_data['rating_id'] = certificate_data['certificate'].map(
    dict(zip(age_rating_data['rating_title'], age_rating_data['rating_id']))
)

# Copying age_rating_data to AgeRating.csv file
#age_rating_data['rating_title'].to_csv('AgeRating.csv', index=False, header=True)


#---------------------------------------------------
# Data for the Director and Movie_Director tables
# Using the movie Rank to keep track of what Age Rating each movie had.
movie_director_table = pd.DataFrame()
director_table = pd.DataFrame()

movie_director_table['movie_id'] = data['rank'].copy()
movie_director_table['director_name'] = data['directors'].copy()

movie_director_table['director_name'] = movie_director_table['director_name'].str.split(',')
movie_director_table = movie_director_table.explode('director_name')
director_table['director_name'] = movie_director_table['director_name'].copy()

# Removing duplicates only from the director_table
director_table = director_table.drop_duplicates()

pk_director_table = [ i + 1 for i in range(director_table.size)]

director_table['director_id'] = pk_director_table

director_table = director_table[['director_id','director_name']]

movie_director_table['director_id'] = movie_director_table['director_name'].map(
    dict(zip(director_table['director_name'], director_table['director_id']))
)

movie_director_table = movie_director_table[['movie_id','director_id']]

#---------------------------------------------------
# Data for the Writers and Movie_Writers tables
# Using the movie Rank to keep track of what Age Rating each movie had.
movie_writers_table = pd.DataFrame()
writers_table = pd.DataFrame()

movie_writers_table['movie_id'] = data['rank'].copy()
movie_writers_table['writer_name'] = data['writers'].copy()

movie_writers_table['writer_name'] = movie_writers_table['writer_name'].str.split(',')
movie_writers_table = movie_writers_table.explode('writer_name')
writers_table['writer_name'] = movie_writers_table['writer_name'].copy()

# Removing duplicates only from the director_table
writers_table = writers_table.drop_duplicates()

pk_writers_table = [ i + 1 for i in range(writers_table.size)]

writers_table['writer_id'] = pk_writers_table

writers_table = writers_table[['writer_id','writer_name']]

movie_writers_table['writer_id'] = movie_writers_table['writer_name'].map(
    dict(zip(writers_table['writer_name'], writers_table['writer_id']))
)

movie_writers_table = movie_writers_table[['movie_id','writer_id']]

#---------------------------------------------------
# Data for the Writers and Movie_Writers tables
# Using the movie Rank to keep track of what Age Rating each movie had.
movie_cast_table = pd.DataFrame()
cast_table = pd.DataFrame()

movie_cast_table['movie_id'] = data['rank'].copy()
movie_cast_table['cast_name'] = data['casts'].copy()

movie_cast_table['cast_name'] = movie_cast_table['cast_name'].str.split(',')
movie_cast_table = movie_cast_table.explode('cast_name')
cast_table['cast_name'] = movie_cast_table['cast_name'].copy()

# Removing duplicates only from the director_table
cast_table = cast_table.drop_duplicates()

pk_cast_table = [ i + 1 for i in range(cast_table.size)]

cast_table['cast_id'] = pk_cast_table

cast_table = cast_table[['cast_id','cast_name']]

movie_cast_table['cast_id'] = movie_cast_table['cast_name'].map(
    dict(zip(cast_table['cast_name'], cast_table['cast_id']))
)

movie_cast_table = movie_cast_table[['movie_id','cast_id']]

#---------------------------------------------------
# Data for the Writers and Movie_Writers tables
# Using the movie Rank to keep track of what Age Rating each movie had.
movie_genre_table = pd.DataFrame()
genre_table = pd.DataFrame()

movie_genre_table['movie_id'] = data['rank'].copy()
movie_genre_table['genre_name'] = data['genre'].copy()

movie_genre_table['genre_name'] = movie_genre_table['genre_name'].str.split(',')
movie_genre_table = movie_genre_table.explode('genre_name')
genre_table['genre_name'] = movie_genre_table['genre_name'].copy()

# Removing duplicates only from the director_table
genre_table = genre_table.drop_duplicates()

pk_genre_table = [ i + 1 for i in range(genre_table.size)]

genre_table['genre_id'] = pk_genre_table

genre_table = genre_table[['genre_id','genre_name']]

movie_genre_table['genre_id'] = movie_genre_table['genre_name'].map(
    dict(zip(genre_table['genre_name'], genre_table['genre_id']))
)

movie_genre_table = movie_genre_table[['movie_id','genre_id']]

#---------------------------------------------------
# Data for the Writers and Movie_Writers tables
# Using the movie Rank to keep track of what Age Rating each movie had.
movie_table = pd.DataFrame()
runtime_orig = pd.DataFrame()
runtime_temp = list()
#movie_table[''] = data[''].copy()

movie_table['movie_id'] = data['rank'].copy()
movie_table['rating_id'] = certificate_data['rating_id'].copy()
movie_table['rank'] = data['rank'].copy()
movie_table['movie_title'] = data['name'].copy()
movie_table['release_date'] = data['year'].copy()
movie_table['score'] = data['rating'].copy()

# Converting runtime from hours and minutes into minutes only
runtime_orig['run_time'] = data['run_time'].copy()
#runtime_temp
for i in runtime_orig['run_time']:
    #print(i)
    if i == "Not Available":    # If the runtime is unavailable
        runtime_temp.append(0)

    elif (i.find("h") >= 0) and (i.find("m") >= 0): # If the runtime format is 0h 00m
        x = (int(i[0]) * 60) + (int(i[int(i.find(" ")):-1]))
        runtime_temp.append(x)
        x = 0

    elif (i.find("h") >= 0) and (i.find("m") < 1): # If the runtime format is 00m
        x = (int(i[0]) * 60)
        runtime_temp.append(x)
        x = 0

    elif (i.find("h") < 1) and (i.find("m") >= 0):
        x = (int(i[0:-1]))
        runtime_temp.append(x)
        x = 0

    else:
        pass



# Adding runtime to the movie table
movie_table['runtime'] = runtime_temp

# Adding the rest of the target fields to the movie table
movie_table['tagline'] = data['tagline'].copy()
movie_table['budget'] = data['budget'].copy()
movie_table['boxoffice'] = data['box_office'].copy()

#print(movie_table.head())


###############################################

# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('/app/src/movies.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

def load_data_into_tables():


    # Inserting data into SQLite Movies Database tables
    try:
        # KEEP and uncomment when done.
        age_rating_data['rating_title'].to_sql('AGE_RATING', conn, if_exists='append', index=False)
        director_table['director_name'].to_sql('DIRECTOR', conn, if_exists='append', index=False)
        writers_table['writer_name'].to_sql('WRITERS', conn, if_exists='append', index=False)
        cast_table['cast_name'].to_sql('CAST', conn, if_exists='append', index=False)
        genre_table['genre_name'].to_sql('GENRE', conn, if_exists='append', index=False)
        movie_table.to_sql('MOVIE', conn, if_exists='append', index=False)
        movie_director_table.to_sql('MOVIE_DIRECTOR', conn, if_exists='append', index=False)
        movie_writers_table.to_sql('MOVIE_WRITERS', conn, if_exists='append', index=False)
        movie_cast_table.to_sql('MOVIE_CAST', conn, if_exists='append', index=False)
        movie_genre_table.to_sql('MOVIE_GENRE', conn, if_exists='append', index=False)

        print("Data successfully loaded into tables.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


if __name__ == '__main__':
    load_data_into_tables()



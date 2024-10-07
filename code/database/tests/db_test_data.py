# Adapted from: How to Show all Columns in the SQLite Database using Python ?
# https://www.geeksforgeeks.org/how-to-show-all-columns-in-the-sqlite-database-using-python/

# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('/app/src/movies.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

target = ['DIRECTOR','WRITERS','CAST','AGE_RATING',
          'GENRE','MOVIE','MOVIE_GENRE','MOVIE_CAST',
          'MOVIE_DIRECTOR','MOVIE_WRITERS']

#drop_target = target.copy()

for i in target:
    # Display columns
    print('\nColumns in '+i+' table:')
    data = cursor.execute('''SELECT * FROM ''' + i)
    for column in data.description:
        print(column[0])

    # Display data
    limit = 5
    #rowNum = 0

    print('\nFirst '+str(limit)+' rows of data in '+i+' table:')
    data = cursor.execute('''SELECT * FROM ''' + i+ ''' LIMIT 5;''')
    for row in data:
        print(row)


# DROPPING All tables after testing.
#print('\nTesting is complete, dropping all tested tables.')

#for j in drop_target:
#    # Display columns
#    print('\n'''+j+' table DROPPED.')
#    data = cursor.execute('''DROP TABLE IF EXISTS ''' +j+''';''')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

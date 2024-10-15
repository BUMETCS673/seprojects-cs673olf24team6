import os
"""This start_movies.py script runs all the files needed to
create the movies.db SQLite database, creates the tables,
and then loads the tables with data."""

exec(open("/database/src/create_movies_db.py").read()) # Creates the database

exec(open("/database/src/create_movies_db_tables.py").read()) # Creates tables

exec(open("/database/src/load_movies_db_data.py").read())

# Path to the file
file_path = "/database/src/movies.db"

# Octal permission: e.g., 0o777 gives full permissions to the owner, group, and others
new_permissions = 0o777

# Change the permissions of the file
os.chmod(file_path, new_permissions)

print(f"Permissions for {file_path} have been changed.")
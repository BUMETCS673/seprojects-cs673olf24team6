""" This file sets up a Flask application to handle movie data queries requests
    from the UI.
    It includes:
        - Establishing a connection to a SQLite database
        - Processing queries for movies based on genre, rating, and release date
        - A single API endpoint to receive frontend requests
"""
import os
import sqlite3
import json
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
CORS(app)


def get_db_connection():
    """Establishes a connection to the SQLite database using the path
       provided by the DATABASE_URL environment variable
       (defaults to '/shared_data/movies.db').
    """

    db_path = os.getenv('DATABASE_URL', '/shared_data/movies.db')
    # pylint: disable=no-member
    app.logger.info(f"Connecting to database at: {db_path}")

    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as database_error:
        # pylint: disable=no-member
        app.logger.info(f"Error connecting to database: {database_error}")
        raise

# Needs comments.
def process_query(date, genre, rating):
    """Receives inputs from backend, formats a SQL statement, runs the
    query, and assigns the data to a dictionary.

    Parameters:
        date (str): The release date threshold (movies released after date)
        genre (str): The genre ID to filter movies by.
        rating (str): The rating ID to filter movies by.

    Returns:
        dict: A dictionary containing a list of movies that match the query
    """

    try:
        # Try to establish a database connection
        conn = get_db_connection()
        genre_int = int(genre)
        rating_int = int(rating)

        query = """
        SELECT movie.*, genre.genre_name, AGE_RATING.rating_title
        FROM movie
        JOIN MOVIE_GENRE ON movie.movie_id = MOVIE_GENRE.movie_id
        JOIN GENRE ON MOVIE_GENRE.genre_id = GENRE.genre_id
        JOIN AGE_RATING ON movie.rating_id = AGE_RATING.rating_id
        WHERE CAST(movie.release_date AS INTEGER) >= ?
        AND GENRE.genre_id = ?
        AND AGE_RATING.rating_id = ?;
        """

        # Try executing the SQL query and fetching data
        cursor = conn.execute(query, (date, genre_int, rating_int))
        rows = cursor.fetchall()

        # Initialize response dictionary
        response_data = {"data": []}

        # Loop through each row and append values that match the filters to response_data
        for row in rows:
            movie_data = {
                "movie_id": row["movie_id"],
                "title": row["movie_title"],
                "release_date": row["release_date"],
                "rank": row["rank"],
                "runtime": row["runtime"],
                "score": row["score"],
                "tagline": row["tagline"],
                "budget": row["budget"],
                "boxoffice": row["boxoffice"],
                "genre": row["genre_name"],
                "rating": row["rating_title"]
            }
            response_data["data"].append(movie_data)

        return response_data

    except sqlite3.Error as e:
        # Handle both database connection and query execution errors
        app.logger.error(f"Database error: {e}")
        return {"error": f"Database error: {str(e)}"}

    finally:
        # Ensure the cursor and connection are always closed, even if an error occurs
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


#Flask route that is used to wait for requests from frontend
@app.route('/api/processQueryRequest', methods=['POST'])
def process_data_request():
    """Based on the user's query from the frontend UI, the process_data_request
     function retrieves the data from the movies.db database."""

    """Processes the incoming POST request from the frontend and queries the database.

    This function receives a JSON payload containing the user's query filters 
    (release date, genre, and rating) and retrieves the matching movie data from the database.
    """

    request_data = request.get_json(silent=True)

    # Check to verify json request is valid
    if not request_data:
        response = jsonify({"error": "Invalid or missing JSON data"})
        response.status_code = 400
        return response

    # pylint: disable=no-member
    app.logger.info(f"Received: {json.dumps(request_data)})")

    # Call query capture data
    response_data = process_query(request_data.get('release_after'),
                                  request_data.get('genre_select'),
                                  request_data.get('genre_select'))
    # pylint: disable=no-member
    app.logger.info(f"Sending response to client: {json.dumps(response_data)}")
    print(f"Sending response to client: {json.dumps(response_data)}")
    return jsonify(response_data), 200


if __name__ == '__main__':
    # Run this application on local host on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

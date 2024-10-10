from flask_cors import CORS
from flask import Flask, request, jsonify
import json
import os
import sqlite3

app = Flask(__name__)
CORS(app)


def get_db_connection():
    db_path = os.getenv('DATABASE_URL', '/shared_data/movies.db')
    app.logger.info(f"Connecting to database at: {db_path}")

    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        app.logger.info(f"Error connecting to database: {e}")
        raise

# Needs comments.
def process_query(date, genre, rating):


    conn = get_db_connection()
    # Jsonify converts values to string we need to reconvert to int to optimize querying.
    genre_int = int(genre)
    rating_int = int(rating)

    # SQL query prep using ? as wildcards to pass values
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

    # Execute query, this may need a try catch block
    cursor = conn.execute(query, (date, genre_int, rating_int))
    rows = cursor.fetchall()

    # Initalize response
    response_data = { "data": [] }


    # Loop through each row and append values that fall within filters
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

    cursor.close()
    conn.close()
    return response_data

#Flask route that is used to wait for requests from frontend
@app.route('/api/processQueryRequest', methods=['POST'])
def process_data_request():
    request_data = request.get_json(silent=True)

    # Check to verify json request is valid
    if not request_data:
        response = jsonify({"error": "Invalid or missing JSON data"})
        response.status_code = 400
        return response

    app.logger.info(f"Received: {json.dumps(request_data)})")

    # Call query capture data
    response_data = process_query(request_data.get('release_after'), request_data.get('genre_select'), request_data.get('genre_select'))

    app.logger.info(f"Sending response to client: {json.dumps(response_data)}")
    print(f"Sending response to client: {json.dumps(response_data)}")
    return jsonify(response_data), 200


if __name__ == '__main__':
    # Run this application on local host on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

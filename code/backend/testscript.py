#from flask_cors import CORS
#from flask import Flask, request, jsonify# Adjust according to your structure

#app = Flask(__name__)
#CORS(app)

#@app.route('/api/getData', methods = ['POST'])


import requests
import json

# Base URL for the API
BASE_URL = 'http://127.0.0.1:5000/api/movies'


def setup_database():
    """Set up the database with test data."""
    # This could be a function that initializes your database with sample data
    pass  # Implement as needed


def test_get_movies_by_genre():
    """Test querying movies by genre."""
    response = requests.get(f'{BASE_URL}?genre=Action')
    assert response.status_code == 200, "Expected status code 200"

    movies = response.json()
    assert isinstance(movies, list), "Expected a list of movies"
    print(f"Movies in Action genre: {movies}")


def test_get_movies_by_country():
    """Test querying movies by country."""
    response = requests.get(f'{BASE_URL}?country=USA')
    assert response.status_code == 200, "Expected status code 200"

    movies = response.json()
    assert isinstance(movies, list), "Expected a list of movies"
    print(f"Movies from USA: {movies}")


def test_get_movies_by_min_rating():
    """Test querying movies by minimum rating."""
    response = requests.get(f'{BASE_URL}?min_rating=7.5')
    assert response.status_code == 200, "Expected status code 200"

    movies = response.json()
    assert isinstance(movies, list), "Expected a list of movies"
    print(f"Movies with rating >= 7.5: {movies}")


def test_get_movies_no_results():
    """Test querying movies with no results."""
    response = requests.get(f'{BASE_URL}?genre=Horror')
    assert response.status_code == 200, "Expected status code 200"

    movies = response.json()
    assert isinstance(movies, list) and len(
        movies) == 0, "Expected no movies found"
    print("No movies found in Horror genre.")


if __name__ == '__main__':
    setup_database()  # Optionally populate the database with test data
    test_get_movies_by_genre()
    test_get_movies_by_country()
    test_get_movies_by_min_rating()
    test_get_movies_no_results()
    print("All tests executed!")
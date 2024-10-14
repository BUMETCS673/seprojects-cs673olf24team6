import pytest
from src.backend import get_db_connection, process_query

# Test that will test the query functionality with mock DB
def test_process_query(mocker):

    # Mock the query function
    mock_conn = mocker.patch('src.backend.get_db_connection')
    mock_cursor = mock_conn.return_value.execute.return_value
    mock_cursor.fetchall.return_value = [
        {
            "movie_id": 1,
            "movie_title": "Test Movie",
            "release_date": "2000",
            "rank": 1,
            "runtime": 120,
            "score": 8.0,
            "tagline": "A test movie",
            "budget": 5000000,
            "boxoffice": 10000000,
            "genre_name": "Drama",
            "rating_title": "PG-13"
        }
    ]

    # call function
    result = process_query(1990, 1, 1)

    # Check if the result matches the expected data structure
    assert result == {
        "data": [
            {
                "movie_id": 1,
                "title": "Test Movie",
                "release_date": "2000",
                "rank": 1,
                "runtime": 120,
                "score": 8.0,
                "tagline": "A test movie",
                "budget": 5000000,
                "boxoffice": 10000000,
                "genre": "Drama",
                "rating": "PG-13"
            }
        ]
    }

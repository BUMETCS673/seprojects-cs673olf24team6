from pytest_mock import mocker
from src import backend
import pytest
import json


@pytest.fixture
def test_client():
    with backend.app.test_client() as client:
        yield client


def test_process_data_request(test_client, mocker):

    mock_process_query = mocker.patch('src.backend.process_query')
    mock_process_query.return_value = {"Python Received": "Test response"}

    incoming_request = {
        'release_after': '1990',
        'genre_select': '1',
        'rating_select': '1'
    }

    mock_process_query = mocker.patch('src.backend.process_query')

    # Set the return value of the mock to simulate a database response
    mock_process_query.return_value = {
        "data": [
            {
                "movie_id": 1,
                "title": "The Shawshank Redemption",
                "release_date": 1994,
                "rank": 1,
                "runtime": 142,
                "score": 9.3,
                "tagline": "Fear can hold you prisoner. Hope can set you free.",
                "budget": 25000000,
                "boxoffice": 28884504,
                "genre": "Drama",
                "rating": "R"
            }
        ]
    }

    # Act: Send the POST request to the Flask app
    response = test_client.post('/api/processQueryRequest',
                                data=json.dumps(incoming_request),
                                content_type='application/json')

    # Assert: Check if the response status code is 200
    assert response.status_code == 200

    # Assert: Check if the response contains the mocked data
    response_data = json.loads(response.data)
    assert 'data' in response_data
    assert len(response_data['data']) == 1
    assert response_data['data'][0]['title'] == "The Shawshank Redemption"
    assert response_data['data'][0]['score'] == 9.3
    assert response_data['data'][0]['genre'] == "Drama"


def test_process_data_request_invalid_json(test_client):
    # Act: Send an invalid request (empty data)
    response = test_client.post('/api/processQueryRequest', data='', content_type='application/json')

    # Assert: Ensure the status code is 400 for invalid or missing JSON
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid or missing JSON data"}
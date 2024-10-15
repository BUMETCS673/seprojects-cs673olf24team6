"""This file `process_query_request_test.py` performs testing for the
backend communication to verify if it is correctly receiving and sending
query requests through the Flask API."""
from pytest_mock import mocker
from src import backend
import pytest
import json


@pytest.fixture
def test_client():
    """This function sets up and yields the Flask test client for testing API
        requests.

    The `pytest.fixture` decorator provides the necessary setup and teardown
    for Flask's test client to ensure isolated test cases. This allows tests
    to simulate sending requests to the backend without needing to run the
    server.

    Yields:
        FlaskClient: A Flask test client instance for simulating requests.
    """
    with backend.app.test_client() as client:
        yield client


def test_process_data_request(test_client, mocker):
    """Tests the `/api/processQueryRequest` endpoint to verify that the
    incoming request matches the expected response. This test ensures that the
    backend processes the data correctly and returns the right results from the
    database.

    The test uses the mocker to mock the `process_query` function in the
    `backend` module, simulating the backend behavior without actually
    connecting to the database.

    Args:
        test_client (FlaskClient): The Flask test client used to simulate API
                                   requests.
        mocker (pytest_mock.mocker): The mocker object to mock functions or methods
                                     during testing.
    """

    # Using mock to mock the process query function
    mock_process_query = mocker.patch('src.backend.process_query')

    # mock request to be sent
    incoming_request = {
        'release_after': '1990',
        'genre_select': '1',
        'rating_select': '1'
    }

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

    #  Send the POST request to the mocked Flask app
    response = test_client.post('/api/processQueryRequest',
                                data=json.dumps(incoming_request),
                                content_type='application/json')

    # Verify that response code is 200 or ok
    assert response.status_code == 200

    # Verify response contains the mocked data in correct structure and length
    response_data = json.loads(response.data)
    assert 'data' in response_data
    assert len(response_data['data']) == 1
    assert response_data['data'][0]['title'] == "The Shawshank Redemption"
    assert response_data['data'][0]['score'] == 9.3
    assert response_data['data'][0]['genre'] == "Drama"

# Scope of this test is to ensure the function can gracefully handle
# incorrectly formed requests.
def test_process_data_request_invalid_json(test_client):
    """Tests the `/api/processQueryRequest` endpoint to ensure that the backend
    can handle incorrectly formatted or invalid JSON data gracefully.

    The test sends an empty request body (invalid JSON) and verifies that the
    API returns a 400 status code and the correct error message.

    Args:
        test_client (FlaskClient): The Flask test client used to simulate API
        requests.
    """

    # Send an invalid request (empty data)
    response = test_client.post('/api/processQueryRequest', data='',
                                content_type='application/json')

    # Verify status code is 400(invalid) and that the json message as expected
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid or missing JSON data"}
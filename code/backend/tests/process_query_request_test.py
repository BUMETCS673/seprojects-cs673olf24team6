from src import backend
import pytest
import json


@pytest.fixture
def test_client():
    with backend.app.test_client() as client:
        yield client


def test_process_data_request(test_client):

        incoming_request = {
            'rank': 1,
            'title': 'Monty Python',
            'release_start': '1955-07-16',
            'release_end': '1999-09-10',
            'score': 10.0,
            'genre_select': 'Legend',
            'rating_select': 'R?',
            'budget': 20,
            'box_office': 829895144000,
            'cast_select': 'All dead',
            'director_select': 'Monty Python?',
            'writer_select': 'Monty Python?'
        }

        response = test_client.post('/processQueryRequest',
                               data=json.dumps(incoming_request),
                               content_type='application/json')

        # Verify that respose is ok type
        assert response.status_code == 200

        # Check if the response contains expected data
        expected_message = (f"Rank: 1, \n"
                            f"Title: Monty Python, \n"
                            f"Release start: 1955-07-16, \n"
                            f"Release end: 1999-09-10, \n"
                            f"Score: 10.0, \n"
                            f"Genre: Legend, \n"
                            f"Rating: R?, \n"
                            f"Budget: 20, \n"
                            f"Box Office: 829895144000, \n"
                            f"Cast: All dead, \n"
                            f"Director: Monty Python?, \n"
                            f"Writer: Monty Python?")

        response_data = json.loads(response.data)

        # Test to ensure the response it correctly formatted
        assert 'Python Received' in response_data
        # Verify test has the expected data
        assert response_data['Python Received'] == expected_message
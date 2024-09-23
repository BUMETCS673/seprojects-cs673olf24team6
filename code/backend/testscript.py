import json
import requests
from flask import Flask, jsonify
from flask_cors import CORS

# Create a test Flask application
test_app = Flask(__name__)
CORS(test_app)

# Define the base URL for the backend API
BASE_URL = 'http://localhost:5000/api/getData'  # Adjust the URL if necessary

# Function to test the getData endpoint
def test_get_data():
    # Input data to send to the API
    input_data = {
        'input1': 'test_value_1',
        'input2': 'test_value_2'
    }

    # Make a POST request to the backend API
    response = requests.post(BASE_URL, json=input_data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        print("Response from API:", response_data)

        # Validate the response message
        expected_message = f"Received input1: {input_data['input1']}, input2: {input_data['input2']}"
        assert response_data['message'] == expected_message, "Response message does not match the expected value."
        print("Response validation passed!")
    else:
        print(f"Error: Received status code {response.status_code}")

# Run the test when this script is executed
if __name__ == '__main__':
    # Start the test application
    with test_app.app_context():
        test_get_data()
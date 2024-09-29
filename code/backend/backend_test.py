# Reference: https://www.geeksforgeeks.org/flask-creating-first-simple
# -application/

import requests
from flask import Flask, jsonify
from flask_cors import CORS

backend_test_app = Flask(__name__)
CORS(backend_test_app)


def test_get_data_endpoint():

    test_input = {
        'input1': 'test_input_1',
        'input2': 'test_input_2'
    }

    response = requests.post('http://0.0.0.0:5000/api/getData', json=test_input)

    if response.status_code == 200:
        response_data = response.json()
        print("Response from backend API:", response_data)

        expected_message = f"Received input1: {test_input['input1']}, input2: {test_input['input2']}"
        assert response_data['message'] == expected_message, "Test Failed!"
        print("Test passed!")
    else:
        print(f"Error: Received status code {response.status_code}")

@backend_test_app.route('/run_backend_test', methods=['GET'])
def run_backend_test():
    test_get_data_endpoint()
    return jsonify({"message": "Backend Test completed!"}), 200


if __name__ == '__main__':
    # Running backend test application on local host on port 5001
    backend_test_app.run(host='0.0.0.0', port=5001, debug=True)

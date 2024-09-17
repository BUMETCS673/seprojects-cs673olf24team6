from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/api/getData', methods=['POST'])
def get_data():
    data = request.json
    input1 = data.get('input1')
    input2 = data.get('input2')

    # Example logic using the inputs
    response_message = f"Received input1: {input1}, input2: {input2}"

    return jsonify({'message': response_message})


if __name__ == '__main__':
    # Run this application on local host on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

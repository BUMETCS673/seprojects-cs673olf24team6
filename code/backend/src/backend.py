from flask_cors import CORS
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
CORS(app)

# TODO Remove when Alex changes have merged
@app.route('/api/getData', methods=['POST'])
def get_data():
    data = request.json
    input1 = data.get('input1')
    input2 = data.get('input2')

    # Example logic using the inputs
    response_message = f"Received input1: {input1}, input2: {input2}"

    return jsonify({'message': response_message})


@app.route('/processQueryRequest', methods=['POST'])
def process_data_request():
    data = request.json

    # Add error handling for invalid or missing JSON
    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    app.logger.info(f"Received: {json.dumps(data)})")

    data_diction = db_query(data)

    response_message = (f"Rank: {data.get('rank')}, \n"
                            f"Title: {data.get('title')}, \n"
                            f"Release start: {data.get('release_start')}, \n"
                            f"Release end: {data.get('release_end')}, \n"
                            f"Score: {data.get('score')}, \n"
                            f"Genre: {data.get('genre_select')}, \n"
                            f"Rating: {data.get('rating_select')}, \n"
                            f"Budget: {data.get('budget')}, \n"
                            f"Box Office: {data.get('box_office')}, \n"
                            f"Cast: {data.get('cast_select')}, \n"
                            f"Director: {data.get('director_select')}, \n"
                            f"Writer: {data.get('writer_select')}")

    return jsonify({'Python Received': response_message}), 200

def db_query(data):
    #conn(db)
    return "Select * {data.get('rank')}"


if __name__ == '__main__':
    # Run this application on local host on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

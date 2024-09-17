from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/getdata', methods=['GET'])
def data():
    return jsonify({'data': "Fish are friends not food"})


if __name__ == '__main__':
    # Run this application on local host on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

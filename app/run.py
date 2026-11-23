from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello World"})


@app.route('/success', methods=['GET'])
def success():
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
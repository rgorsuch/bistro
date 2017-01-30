
from flask import Flask, request
from flask import jsonify


app=Flask(__name__)


@app.route("/", methods=['GET'])
def get_bistro():
    return jsonify({'project':'bistro', 'version':'1.0.0'})

@app.route("/", methods=['POST'])
def post_bistro():
    return jsonify({'method': 'POST'})


@app.route("/", methods=['PUT'])
def put_bistro():
    return jsonify({'method': 'PUT'})


@app.route("/", methods=['DELETE'])
def delete_bistro():
    return jsonify({'method': 'PUT'})


if __name__=="__main__":
    app.run()





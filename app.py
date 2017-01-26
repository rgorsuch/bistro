
from flask import Flask
from flask import jsonify


app=Flask(__name__)


@app.route("/")
def hello():
    return jsonify({'project':'bistro', 'version':'1.0.0'})


if __name__=="__main__":
    app.run()






from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return "{ \"project\":\"bistro\" \"version\":\"1.0.0\"}"

if __name__=="__main__":
    app.run()




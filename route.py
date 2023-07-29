from flask import Flask
from moncar import *
app=Flask(__name__)
@app.route("/mona")
def mona():
    mon()
    return {"members":["m1","m2","m3"]}

@app.route("/reseta")
def reseta():
    reset()
    return {"members": ["m1", "m2", "m3"]}
if __name__=="__main__":
    app.run(debug=True)
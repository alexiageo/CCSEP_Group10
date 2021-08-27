#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def CCSEP_Group10():
    return 'This the samle website of ccsep group10 assignment'


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)

#!/usr/bin/python3
'''A script to start flask
Display a message
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Display greeting message'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays a new page HBNB'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

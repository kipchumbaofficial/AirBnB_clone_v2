#!/usr/bin/python3
'''A script to start flask
Display a message
'''
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Display greeting message'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays a new page HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''Applies use of a variable'''
    formated_text = text.replace("_", " ")
    return f"C {escape(formated_text)}"


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def is_python(text):
    '''Python is cool'''
    formated_text = text.replace("_", " ")
    return f"Python {escape(formated_text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Number specification'''
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

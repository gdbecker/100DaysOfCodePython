# 100 Days of Code: Python
# June 14, 2022
# Building web app with Flask framework

## Getting the server up and going
# Use Command Prompt
# cd to the directory with server file
# set FLASK_APP=filename.py
# flask run

# Copied from Flask site
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Function decorator example
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

# Some new decorator functions
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

@delay_decorator
def say_hello():
    return "Hello"

@app.route('/bye')
@make_bold
@make_emphasis
def say_bye():
    return "Bye!"

def say_greeting():
    print("How are you?")

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
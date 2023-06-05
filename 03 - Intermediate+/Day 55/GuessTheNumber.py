# 100 Days of Code: Python
# June 14, 2022
# Guess the Number web app
# with Flask

# Import modules
import random
from flask import Flask

# Set up Flask app
app = Flask(__name__)

# Number to guess
answer = random.randint(0,9)

# HTML pages
@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<guess>")
def guess_result(guess):
    global answer
    if int(guess) < answer:
        return "<h1 style='color:blue'>Too low, try again!</h1><img src='https://media.giphy.com/media/7z45HnpdJL2TK/giphy-downsized-large.gif'>"
    elif int(guess) > answer:
        return "<h1 style='color:red'>That's too high, try again!</h1><img src='https://media.giphy.com/media/jMYfKgEDZQPYMFgBHZ/giphy.gif'>"
    elif int(guess) == answer:
        return "<h1 style='color:purple'>You found me! Congrats!!</h1><img src='https://media.giphy.com/media/Y4pAQv58ETJgRwoLxj/giphy-downsized-large.gif'>"

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
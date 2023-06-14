# 100 Days of Code: Python
# June 15, 2022
# practice using day 41-44 personal site with Flask
# with Flask

# Import modules
from flask import Flask, render_template

# Set up Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
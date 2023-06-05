# 100 Days of Code: Python
# June 15, 2022
# blog site project with Flask

# Import modules
from post import Post
from flask import Flask, render_template
import requests
import datetime

# Set up Flask app
app = Flask(__name__)

# Make list of Post objects
current_year = datetime.datetime.now().year
blog_url = "https://api.npoint.io/82975389c85afb34e389"
all_posts = requests.get(blog_url).json()
post_list = []
for p in all_posts:
    post_list.append(Post(p["id"], p["title"], p["subtitle"], p["body"]))

@app.route("/")
def home():
    return render_template("index.html", year=current_year, posts=post_list)

@app.route("/post/<blog_id>")
def post(blog_id):
    selected_post = None
    for p in post_list:
        if p.id == int(blog_id):
            selected_post = p
    return render_template("post.html", year=current_year, post=selected_post)

# Challenge during module
@app.route("/guess/<name>")
def guess(name):
    global current_year

    parameters = {
        "name": name
    }
    response = requests.get(url="https://api.agify.io", params=parameters)
    response.raise_for_status()
    data = response.json()
    age = data["age"]

    response = requests.get(url="https://api.genderize.io/", params=parameters)
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]

    return render_template("guess.html", year=current_year, name=name.title(), age=age, gender=gender)

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
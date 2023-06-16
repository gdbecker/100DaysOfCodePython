# 100 Days of Code: Python
# June 18-19, 2022
# Blog site project with Flask
# Updated from Day 57 with Bootstrap

# Import modules
from post import Post
from flask import Flask, render_template, request
import requests
import datetime
import smtplib
from decouple import config

# Email info
smtp_gmail = "smtp.gmail.com"
email_gmail = config("email_gmail")
app_password_gmail = config("app_password_gmail") # had to get because of new security settings
password_gmail = config("password_gmail")

smtp_yahoo = config("smtp_yahoo")
email_yahoo = config("email_yahoo")
password_yahoo = config("password_yahoo")

# Set up Flask app
app = Flask(__name__)

# Make list of Post objects
current_year = datetime.datetime.now().year

# My own API link I made for this project
blog_url = "https://api.npoint.io/738161d0e606d1f60a3f"
all_posts = requests.get(blog_url).json()
post_list = []
for p in all_posts:
    post_list.append(Post(p["id"], p["title"], p["subtitle"], p["body"], p["author"], p["date"], p["image_url"]))

@app.route("/")
def home():
    return render_template("index.html", year=current_year, posts=post_list)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        form_name = request.form["name"]
        form_email = request.form["email"]
        form_phone = request.form["phone"]
        form_message = request.form["message"]

        # Send email with form info
        with smtplib.SMTP(smtp_gmail) as connection:
            connection.starttls()  # secures the connection
            connection.login(user=email_gmail, password=app_password_gmail)
            connection.sendmail(from_addr=email_gmail, to_addrs=email_gmail, msg=f"Subject: New Message!\n\nName: {form_name}\n\nEmail: {form_email}\n\nPhone: {form_phone}\n\nMessage: {form_message}")

        return render_template("contact.html", submitted=True)

@app.route("/post/<blog_id>")
def post(blog_id):
    selected_post = None
    for p in post_list:
        if p.id == int(blog_id):
            selected_post = p
    return render_template("post.html", year=current_year, post=selected_post)

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
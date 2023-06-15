# 100 Days of Code: Python
# June 22, 2022
# Blog site project with Flask
# Updated from Day 59-60 with database and REST methods

# Import modules
from post import Post
import requests
from datetime import datetime, date
import smtplib
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

# Email info
smtp_gmail = "smtp.gmail.com"
email_gmail = "garrettbeckerpython1@gmail.com"
app_password_gmail = "mznjpioosjdjxcaz" # had to get because of new security settings
password_gmail = "Pats1982!!"

smtp_yahoo = "smtp.mail.yahoo.com"
email_yahoo = "garrettbeckerpython1@yahoo.com"
password_yahoo = "manbmqmvtzykfvgt!!"

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
ckeditor = CKEditor(app)
Bootstrap(app)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure BlogPost table in database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# WTF-form to make a new post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# Make the database -> comment out when done
# db.create_all()

# Get current date info
today = date.today()
date = today.strftime("%B %d, %Y")
current_year = datetime.now().year

# Old: replacing with the posts database
# Make list of Post objects
# My own API link I made for this project
# blog_url = "https://api.npoint.io/738161d0e606d1f60a3f"
# all_posts = requests.get(blog_url).json()
# post_list = []
# for p in all_posts:
#     post_list.append(Post(p["id"], p["title"], p["subtitle"], p["body"], p["author"], p["date"], p["img_url"]))

# New: Get all posts from database
def get_all_posts():
    all_posts_list = []
    all_posts_db = db.session.query(BlogPost).all()

    for db_post in all_posts_db:
        p = Post(
            db_post.id,
            db_post.title,
            db_post.subtitle,
            db_post.body,
            db_post.author,
            db_post.date,
            db_post.img_url
        )
        all_posts_list.append(p)
    return all_posts_list

# Get a post by id
def get_post_by_id(blog_id):
    selected_post = None
    post_list = get_all_posts()
    for p in post_list:
        if p.id == int(blog_id):
            selected_post = p
    return selected_post

# Flask routes
@app.route("/")
def home():
    post_list = get_all_posts()
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
    selected_post = get_post_by_id(blog_id)
    return render_template("post.html", year=current_year, post=selected_post)

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if request.method == "GET":
        return render_template("make-post.html", form=form, is_new_post=True)
    elif request.method == "POST":
        new_post = BlogPost(
            title=request.form["title"],
            subtitle=request.form["subtitle"],
            date=date,
            body=request.form["body"],
            author=request.form["author"],
            img_url=request.form["img_url"]
        )
        db.session.add(new_post)
        db.session.commit()
        post_list = get_all_posts()
        return redirect(url_for("home", year=current_year, posts=post_list))

@app.route("/edit-post/<blog_id>", methods=["GET", "POST"])
def edit_post(blog_id):
    selected_post = get_post_by_id(blog_id)
    print(selected_post.img_url)
    form = CreatePostForm(obj=selected_post)
    if request.method == "GET":
        return render_template("make-post.html", post=selected_post, form=form, is_new_post=False)
    elif request.method == "POST":
        post_to_update = BlogPost.query.filter_by(id=int(blog_id)).first()
        post_to_update.title = request.form["title"]
        post_to_update.subtitle = request.form["subtitle"]
        post_to_update.body = request.form["body"]
        post_to_update.author = request.form["author"]
        post_to_update.img_url = request.form["img_url"]
        db.session.commit()

        post_list = get_all_posts()
        return redirect(url_for("home", year=current_year, posts=post_list))

@app.route("/delete/<blog_id>")
def delete(blog_id):
    db.session.query(BlogPost).filter(BlogPost.id == int(blog_id)).delete()
    db.session.commit()
    post_list = get_all_posts()
    return redirect(url_for("home", year=current_year, posts=post_list))

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
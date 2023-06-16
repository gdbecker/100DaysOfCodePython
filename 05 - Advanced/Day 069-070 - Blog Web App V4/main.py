# 100 Days of Code: Python
# June 23, 2022
# Blog site project with Flask
# Updated from Day 67 with authentication for users

# Import modules
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import requests
from datetime import datetime, date
import smtplib
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Get current date info
today = date.today()
date = today.strftime("%B %d, %Y")
current_year = datetime.now().year

# Set up Gravatar icons for comments
gravatar = Gravatar(app,
                    size=50,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None
        )

# Configure User table in database
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # This will act like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")

    comments = relationship("Comment", back_populates="comment_author")

# Configure BlogPost table in database
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="posts")

    img_url = db.Column(db.String(250), nullable=False)

    # ***************Parent Relationship************* #
    comments = relationship("Comment", back_populates="parent_post")

# Configure Comment table in database
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # ***************Child Relationship************* #
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.Text, nullable=False)

# Make the database -> comment out when done
# db.create_all()

# Required: call-back function to get a user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Get all posts from database
def get_all_posts():
    return db.session.query(BlogPost).all()

# Get a post by id
def get_post_by_id(blog_id):
    return BlogPost.query.filter_by(id=int(blog_id)).first()

# Flask routes
@app.route("/")
def home():
    post_list = get_all_posts()
    return render_template("index.html", posts=post_list)

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

@app.route("/post/<blog_id>", methods=["GET", "POST"])
def post(blog_id):
    form = CommentForm()
    selected_post = get_post_by_id(blog_id)
    print(selected_post.comments)
    if request.method == "GET":
        return render_template("post.html", post=selected_post, form=form)
    elif request.method == "POST":
        new_comment = Comment(
            author_id=current_user.id,
            post_id=blog_id,
            text=request.form["comment"]
        )
        db.session.add(new_comment)
        db.session.commit()
        return render_template("post.html", post=selected_post, form=form)

@app.route("/new-post", methods=["GET", "POST"])
@login_required
def new_post():
    if current_user.id == 1:
        form = CreatePostForm()
        if request.method == "GET":
            return render_template("make-post.html", form=form, is_new_post=True)
        elif request.method == "POST":
            new_post = BlogPost(
                title=request.form["title"],
                subtitle=request.form["subtitle"],
                date=date,
                body=request.form["body"],
                author=current_user,
                img_url=request.form["img_url"]
            )
            db.session.add(new_post)
            db.session.commit()
            post_list = get_all_posts()
            return redirect(url_for("home", posts=post_list))
    else:
        post_list = get_all_posts()
        return redirect(url_for("home", posts=post_list))

@app.route("/edit-post/<blog_id>", methods=["GET", "POST"])
@login_required
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
        # post_to_update.author = request.form["author"]
        post_to_update.img_url = request.form["img_url"]
        db.session.commit()

        post_list = get_all_posts()
        return redirect(url_for("home", posts=post_list))

@app.route("/delete/<blog_id>")
@login_required
def delete(blog_id):
    db.session.query(BlogPost).filter(BlogPost.id == int(blog_id)).delete()
    db.session.commit()
    post_list = get_all_posts()
    return redirect(url_for("home", posts=post_list))

@app.route("/delete-comment/")
@login_required
def delete_comment():
    comment_id = request.args.get("comment_id")
    blog_id = request.args.get("blog_id")
    db.session.query(Comment).filter(Comment.id == int(comment_id)).delete()
    db.session.commit()
    form = CommentForm()
    selected_post = get_post_by_id(blog_id)
    return render_template("post.html", post=selected_post, form=form)

# Authentication routes
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("register.html", form=form)
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user != None:
            flash("You've already signed up with that email. Login instead!")
            return redirect(url_for("login"))
        else:
            new_user = User(
                email=request.form["email"],
                password=generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8),
                name=request.form["name"]
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("home"))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    elif request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user == None:
            flash("That email does not exist! Please try again.")
            return redirect(url_for("login"))
        elif check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("home"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Runs the server without typing into command prompt
if __name__ == "__main__":
    app.run(debug=True)
# 100 Days of Code: Python
# June 20, 2022
# Flask project: virtual bookshelf web app
# practicing what I've learned

# Import modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import sqlite3

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

# Set up database
db = SQLAlchemy(app)

# Book table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), unique=False, nullable=False)

# With SQLAlchemy to make
# db.create_all()

# Old first way to make: with sqlite3 package
# db = sqlite3.connect("library.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# ---------------

# CRUD examples with SQLAlchemy
# # Read All Records
# all_books = db.session.query(Book).all()

# # Read A Particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()

# # Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# # Update A Record By PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# # Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

# Get all books from database
def get_all_books():
    all_books_list = []
    all_books_db = db.session.query(Book).all()
    for db_book in all_books_db:
        b = {
            "id": db_book.id,
            "title": db_book.title,
            "author": db_book.author,
            "rating": db_book.rating
        }
        all_books_list.append(b)
    return all_books_list

# Flask routes
@app.route('/')
def home():
    all_books_list = get_all_books()
    return render_template("index.html", books=all_books_list)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        all_books_list = get_all_books()
        return render_template("index.html", books=all_books_list)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        selected_book = None
        all_books_list = get_all_books()
        for b in all_books_list:
            if b["id"] == int(id):
                selected_book = b
        return render_template("edit.html", book=selected_book)
    elif request.method == "POST":
        db.session.query(Book). \
            filter(Book.id == request.form["book_id"]). \
            update({"rating": request.form["rating"]})
        db.session.commit()

        all_books_list = get_all_books()
        return render_template("index.html", books=all_books_list)

@app.route("/delete/<id>")
def delete(id):
    selected_book = None
    all_books_list = get_all_books()
    for b in all_books_list:
        if b["id"] == int(id):
            selected_book = b
    db.session.query(Book). \
        filter(Book.id == id).delete()
    db.session.commit()

    all_books_list = get_all_books()
    return render_template("index.html", books=all_books_list)

if __name__ == "__main__":
    app.run(debug=True)
# 100 Days of Code: Python
# June 21, 2022
# Flask project: top 10 movies web app
# practicing what I've learned

# Import modules
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests

# TMDB Info
API_KEY = "81c491bbbc3ebfcf3e8caebb08ef74f5"
SEARCH_MOVIES_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/"

# Set up Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'harrypotterravenclaw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

# Set up database
db = SQLAlchemy(app)

# Movies table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer(), unique=False, nullable=False)
    description = db.Column(db.String(750), unique=False, nullable=False)
    rating = db.Column(db.Float(), unique=False, nullable=True)
    ranking = db.Column(db.Integer(), unique=False, nullable=True)
    review = db.Column(db.String(750), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

# Make the database -> comment out when done
# db.create_all()

# Manually add first movie -> comment out when done
# first_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(first_movie)
# db.session.commit()

# Form for adding new movie
class NewMovieForm(FlaskForm):
    title = StringField(label='Movie Title')
    submit = SubmitField('Add Movie')

# Form for editing a movie
class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating (out of 10, ex: 7.5)')
    review = StringField(label='Your Review')
    submit = SubmitField('Submit')

# Get all movies from database
def get_all_movies():
    all_movies_list = []
    all_movies_db = db.session.query(Movie).order_by(Movie.rating.desc())
    x = 1
    for movie in all_movies_db:
        movie.ranking = x
        x += 1
    db.session.commit()

    for db_movie in all_movies_db:
        m = {
            "id": db_movie.id,
            "title": db_movie.title,
            "year": db_movie.year,
            "description": db_movie.description,
            "rating": db_movie.rating,
            "ranking": db_movie.ranking,
            "review": db_movie.review,
            "img_url": db_movie.img_url,
        }
        all_movies_list.append(m)
    return all_movies_list

# Flask routes
@app.route("/")
def home():
    all_movies_list = get_all_movies()
    return render_template("index.html", movies=all_movies_list)

@app.route("/search", methods=["GET", "POST"])
def search():
    form = NewMovieForm()
    if request.method == "GET":
        return render_template("add.html", form=form)
    elif request.method == "POST":
        new_movie_title = form.title.data
        parameters = {
            "api_key": API_KEY,
            "query": new_movie_title
        }
        response = requests.get(url=SEARCH_MOVIES_URL, params=parameters)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template("select.html", results=data)

@app.route("/add/<tmdb_id>")
def add(tmdb_id):
    parameters = {
        "api_key": API_KEY
    }
    response = requests.get(url=f"{MOVIE_DETAILS_URL}{tmdb_id}", params=parameters)
    response.raise_for_status()
    data = response.json()

    new_movie = Movie(
        title=data["original_title"],
        year=int(data["release_date"][0:4]),
        description=data["overview"],
        img_url="https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    )
    db.session.add(new_movie)
    db.session.commit()

    selected_movie = None
    all_movies_list = get_all_movies()
    for m in all_movies_list:
        if m["title"] == new_movie.title:
            selected_movie = m

    form = RateMovieForm()
    return redirect(url_for("edit", id=selected_movie["id"]))

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    if request.method == "GET":
        selected_movie = None
        all_movies_list = get_all_movies()
        for m in all_movies_list:
            if m["id"] == int(id):
                selected_movie = m
        return render_template("edit.html", movie=selected_movie, form=form)
    elif request.method == "POST":
        movie_to_update = Movie.query.filter_by(id=int(id)).first()
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()

        all_movies_list = get_all_movies()
        return render_template("index.html", movies=all_movies_list)

@app.route("/delete/<id>")
def delete(id):
    db.session.query(Movie).filter(Movie.id == id).delete()
    db.session.commit()

    all_movies_list = get_all_movies()
    return render_template("index.html", movies=all_movies_list)

if __name__ == '__main__':
    app.run(debug=True)

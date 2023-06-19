# 100 Days of Code: Python
# August 13, 2022
# RESTful API service using public NASA API
# Source: https://api.nasa.gov/index.html

# Import modules
from flask import Flask, jsonify, render_template, request
import requests
from datetime import datetime, timedelta
from decouple import config

# Set up Flask app
app = Flask(__name__)

# Function to make a 0 or 1 a Boolean valaue
def make_bool(val: int) -> bool:
    return bool(int(val))

# NASA API info (for all requests)
API_KEY = config("API_KEY")

# Flask routes
@app.route("/")
def home():
    return render_template("index.html")

# GET: Astronomy picture of the day
@app.route("/astro", methods=["GET"])
def astro():
    url_astro = "https://api.nasa.gov/planetary/apod"
    parameters_astro = {
        "api_key": API_KEY
    }
    response = requests.get(url=url_astro, params=parameters_astro)
    data = response.json()
    print(data)
    return render_template("astro.html", data=data)

# GET: Mars weather data
@app.route("/mars-weather", methods=["GET"])
def mars_weather():
    url_mars_weather = "https://api.nasa.gov/insight_weather/"
    parameters_mars_weather = {
        "api_key": API_KEY,
        "version": "1.0",
        "feedtype": "json"
    }
    response = requests.get(url=url_mars_weather, params=parameters_mars_weather)
    data = response.json()
    return data

# GET: Mars rover photos
@app.route("/mars-photos/<rover>/<sol>", methods=["GET"])
def mars_photos(rover, sol):
    url_mars_photos = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos/"
    parameters_mars_photos = {
        "api_key": API_KEY,
        "sol": sol
    }
    response = requests.get(url=url_mars_photos, params=parameters_mars_photos)
    data = response.json()
    return data

# GET: Space weather notifications
@app.route("/space-weather", methods=["GET"])
def space_weather():
    today = datetime.today()
    last_week = today - timedelta(days=7)
    today = today.strftime("%Y-%m-%d")
    last_week = last_week.strftime("%Y-%m-%d")

    url_space_weather = "https://api.nasa.gov/DONKI/notifications"
    parameters_space_weather = {
        "api_key": API_KEY,
        "startDate": last_week,
        "endDate": today,
        "type": "all"
    }

    response = requests.get(url=url_space_weather, params=parameters_space_weather)
    data = [entry for entry in response.json()]
    return render_template("space_weather.html", data=data)

# GET: Asteroids nearest to Earth
@app.route("/asteroids", methods=["GET"])
def asteroids():
    today = datetime.today()
    last_week = today - timedelta(days=7)
    today = today.strftime("%Y-%m-%d")
    last_week = last_week.strftime("%Y-%m-%d")

    url_asteroids = "https://api.nasa.gov/neo/rest/v1/feed"
    parameters_asteroids = {
        "api_key": API_KEY,
        "startDate": last_week,
        "endDate": today
    }

    response = requests.get(url=url_asteroids, params=parameters_asteroids)
    data = response.json()["near_earth_objects"][today]
    return render_template("asteroids.html", data=data, date=today)

if __name__ == '__main__':
    app.run(debug=True)
# 100 Days of Code: Python
# June 1, 2022
# Webscraping the top 100 movies of all time

# Import modules
from bs4 import BeautifulSoup
import requests

# Make soup for Empire's movie list
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
wp = response.text
soup = BeautifulSoup(wp, "html.parser")

# Get list of movies and their ranks
movies_list = soup.findAll(name="h3", class_="title")
movie_titles = [m.getText() for m in movies_list]
movie_titles.reverse()

# Print all movies
for m in movie_titles:
    print(m)
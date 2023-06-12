# 100 Days of Code: Python
# June 2, 2022
# Make Spotify playlist for top Billboard 100 songs of a given year
# Using web scraping and Spotify & Spotipy APIs and docs

# Import modules
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from decouple import config

# Get year input from user
date_input = input("What year would you like to musically time travel to? Input in format YYYY-MM-DD: ")
year = date_input[0:4]

# Get data from Billboard site
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Get top 100 songs
songs_list = soup.select(selector="li h3", class_="title-of-a-story")
temp = [s.getText().strip() for s in songs_list]
song_titles = temp[0:100]

# Get top 100 artists
artists_list = soup.select("span.c-label.a-no-trucate")
temp = [a.getText().strip() for a in artists_list]
artists_names = temp[0:100]

# Spotify info and authentication
REDIRECT_URL = config("REDIRECT_URL")
SCOPE = config("SCOPE")
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope=SCOPE
    )
)

user = sp.current_user()
user_id = user["id"]

# Get URLs for songs
search_years = f"{int(year)-1}-{year}"
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{search_years}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        #print(song_uris)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# Create new Spotify playlist
playlist_name = f"{date_input} Billboard 100"
new_playlist = sp.user_playlist_create(user_id, name=playlist_name, public=False)
playlist_id = new_playlist["id"]

# Add songs to playlist
sp.playlist_add_items(playlist_id, song_uris, position=None)
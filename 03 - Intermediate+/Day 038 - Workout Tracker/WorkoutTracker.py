# 100 Days of Code: Python
# May 28, 2022
# Keep track of workouts with Google Sheets

# Import modules
import requests
from datetime import datetime
from decouple import config

# Today date/time info
now = datetime.now()
today = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

# NutritionIX info
USERNAME = config("USERNAME")
APP_ID = config("APP_ID")
NIX_KEY = config("NIX_KEY")

nix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": NIX_KEY
}

exercise_post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Post exericse info
query = input("Tell me what exercises you did: ")
nix_parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 72.57,
    "height_cm": 173,
    "age": 27
}
response = requests.post(url=exercise_post_endpoint, data=nix_parameters, headers=nix_headers)
exercise_data = response.json()["exercises"][0]
exercise = exercise_data["name"].title()
duration = str(exercise_data["duration_min"])
calories = str(exercise_data["nf_calories"])

# Post exercise info to Google Sheets via Sheety
sheety_headers = {
    "Authorization": config("BEARER")
}
sheety_post_endpoint = "https://api.sheety.co/7f8e7cb4219a99c4897c416248a725ef/workoutTracker/workouts"
sheety_parameters = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
response = requests.post(url=sheety_post_endpoint, json=sheety_parameters, headers=sheety_headers)
print(response.text)

# Heads up
print("Visit https://docs.google.com/spreadsheets/d/1X8gW7bUnNfDUSbygMfEZL8mr0GAslHDSh3j2dlN9zHg/edit#gid=0 to see the results!")
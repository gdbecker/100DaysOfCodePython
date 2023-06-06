# 100 Days of Code: Python
# May 26, 2022
# App to send SMS alert if it's going to be raining today

# Import modules
import requests
from twilio.rest import Client

# Info
# OpenWeather API key
api_key = "1b097d58f77c78ab34d2e237c8d98729"
twilio_account_sid = "ACf99c4a24825bb34ae964b5e605cbbcb0"
twilio_auth_token = "be435f26191a3a0ca4b9be0cebb51dc9"

# Getting data from OpenWeather one call api
url = "https://api.openweathermap.org/data/2.5/onecall"
my_lat = 35.227085
my_long = -80.843124
my_exclude = "current,minutely,daily"
parameters = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": my_exclude,
    "appid": api_key
}

# Getting hourly forecast for the next 48 hours
response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]

# Go through the first 12 hours and check for rain
for index in range(0,12):
    hour_data = weather_data[index]
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

# Set up Twilio
if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
        body="It will rain today, remember to bring an umbrella!",
        from_="+19785413241",
        to="+19198961843"
    )
    print(message.status)
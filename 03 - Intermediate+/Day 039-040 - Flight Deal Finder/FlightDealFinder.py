# 100 Days of Code: Python
# May 28, 2022
# Search your Google Sheets of flights you want, send text alerts when they're cheaper!
# Scratching this project because of the limited free flight API's there are out there :(

# Import modules
import requests
from datetime import datetime
from twilio.rest import Client
from decouple import config

# Sheety info
sheety_get_endpoint = "https://api.sheety.co/7f8e7cb4219a99c4897c416248a725ef/flightFinder/flights"
sheety_headers =  {
    "Authorization": "Basic bnVsbDpudWxs"
}

# AviationStack flight finder info (I couldn't get Tequila/Kiwi to work so I found this one)
as_key = config("as_key")
as_endpoint = config("as_endpoint")

# Twilio info
twilio_account_sid = config("twilio_account_sid")
twilio_auth_token = config("twilio_auth_token")

# ONE: get data from Google Sheets with desired flights
response = requests.get(url=sheety_get_endpoint, headers=sheety_headers)
flight_sheet_data = response.json()["flights"]

# TWO: search flights on AviationStack
for dict in flight_sheet_data:
    as_params = {
        "access_key": as_key,
        "dep_iata": dict["fromIataCode"],
        "arr_iata": dict["toIataCode"]
    }
    response = requests.get(url=as_endpoint, params=as_params)
    print(response.text)




# 100 Days of Code: Python
# May 28, 2022
# Search your Google Sheets of flights you want, send text alerts when they're cheaper!
# Scratching this project because of the limited free flight API's there are out there :(

# Import modules
import requests
from datetime import datetime
from twilio.rest import Client

# Sheety info
sheety_get_endpoint = "https://api.sheety.co/7f8e7cb4219a99c4897c416248a725ef/flightFinder/flights"
sheety_headers =  {
    "Authorization": "Basic bnVsbDpudWxs"
}

# # Amadeus flight finder info (I couldn't get Tequila/Kiwi to work so I found this one)
# a_key = "BBNWrtGnsYGwEMqBYH8DWQl2ELlfuRSg"
# a_secret = "rRGXCqaIfpXAb5wB"
# a_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
# a_headers = {
#     "authorization": "Bearer qeAzQLwgEn6AdDRDlvVoiVSOmMGD"
# }

# AviationStack flight finder info (I couldn't get Tequila/Kiwi to work so I found this one)
as_key = "a5f9853de00d8cfe9d72599f1957a59f"
as_endpoint = "http://api.aviationstack.com/v1/flights"

# Twilio info
twilio_account_sid = "ACf99c4a24825bb34ae964b5e605cbbcb0"
twilio_auth_token = "be435f26191a3a0ca4b9be0cebb51dc9"

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




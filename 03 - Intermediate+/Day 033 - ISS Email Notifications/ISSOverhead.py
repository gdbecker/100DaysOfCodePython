# 100 Days of Code: Python
# May 24, 2022
# ISS Overhead Notifier project
# Using the ISS API to get data

'''
Dummy email accounts info:
Gmail --
garrettbeckerpython1@gmail.com

Yahoo --
garrettbeckerpython1@yahoo.com
'''

# Import modules
import requests
from datetime import datetime as dt, timezone
import smtplib
from decouple import config

# Email info
smtp_gmail = config("smtp_gmail")
email_gmail = config("email_gmail")
password_gmail = config("password_gmail")

smtp_yahoo = config("smtp_yahoo")
email_yahoo = config("email_yahoo")
password_yahoo = config("password_yahoo")

# My location
LAT = 35.118279
LONG = -80.720207

# Get data from ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Check if my position is within +/- 5 dgerees of ISS
if (LAT >= (iss_latitude - 5) and LAT <= (iss_latitude + 5)) and (LONG >= (iss_longitude - 5) and LONG <= (iss_longitude + 5)):
    is_within = True
else:
    is_within = False

parameters = {
    "lat":LAT,
    "lng":LONG,
    "formatted": 0
}

# Get the sunrise/sunset info based on my location
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

if sunset == 0:
    sunset = 24

time_now = dt.now(timezone.utc)
hour_now = time_now.hour

# ^had to convert my time to utc time to be able to compare hours (API returned times in UTC zone)

# Check if my current time is at night
if hour_now <= sunrise or hour_now >= sunset:
    is_night = True
else:
    is_night = False

print(is_night)

# Send email to look up
if is_within and is_night:
    with smtplib.SMTP(smtp_gmail) as connection:
        connection.starttls() # secures the connection
        connection.login(user=email_gmail, password=password_gmail)
        connection.sendmail(from_addr=email_gmail, to_addrs=email_yahoo, msg=f"Subject: ISS!\n\nLOOK UP!")


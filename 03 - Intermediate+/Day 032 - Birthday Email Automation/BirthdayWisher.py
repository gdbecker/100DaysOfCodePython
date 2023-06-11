# 100 Days of Code: Python
# May 24, 2022
# Automate sending bday emails with python!

'''
Dummy email accounts info:
Gmail --
garrettbeckerpython1@gmail.com

Yahoo --
garrettbeckerpython1@yahoo.com
'''

'''
Note: Make sure that the birthdays in .csv file are set to today in order to see the birthday message!
'''

# Import modules
import smtplib
import random
import datetime as dt
import pandas
from decouple import config

# SMTP info
smtp_gmail = config("smtp_gmail")
email_gmail = config("email_gmail")
password_gmail = config("password_gmail")

smtp_yahoo = config("smtp_yahoo")
email_yahoo = config("email_yahoo")
password_yahoo = config("password_yahoo")

# Import a random latter template
letter_num = random.randint(1,3)
letter_file = open(f"letter_templates/letter_{letter_num}.txt", "r")
letter_contents = letter_file.read()
PLACEHOLDER = "[NAME]"

# Read in contacts and birthday info
birthday_info = pandas.read_csv("birthdays.csv")

# Get today's info
now = dt.datetime.now()
month_now = now.month
day_now = now.day

# Loop through each birthday and see if it's today
# If so, send a birthday message
for index,row in birthday_info.iterrows():
    if row["month"] == month_now and row["day"] == day_now:
        name = row["name"]
        to_email = row["email"]
        letter_contents = letter_contents.replace(PLACEHOLDER, name)

        with smtplib.SMTP(smtp_gmail) as connection:
            connection.starttls()
            connection.login(user=email_gmail, password=password_gmail)
            connection.sendmail(from_addr=email_gmail, to_addrs=to_email, msg=f"Subject: HAPPY BIRTHDAY!\n\n{letter_contents}")
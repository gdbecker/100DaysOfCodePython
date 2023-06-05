# 100 Days of Code: Python
# May 24, 2022
# Automate sending bday emails with python!

'''
Dummy email accounts info:
Gmail --
garrettbeckerpython1@gmail.com
Pats1982!!

Yahoo --
garrettbeckerpython1@yahoo.com
Pats1982!!
'''

# Import modules
import smtplib
import random
import datetime as dt
import pandas

# SMTP info
smtp_gmail = "smtp.gmail.com"
email_gmail = "garrettbeckerpython1@gmail.com"
password_gmail = "Pats1982!!"

smtp_yahoo = "smtp.mail.yahoo.com"
email_yahoo = "garrettbeckerpython1@yahoo.com"
password_yahoo = "manbmqmvtzykfvgt!!"

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
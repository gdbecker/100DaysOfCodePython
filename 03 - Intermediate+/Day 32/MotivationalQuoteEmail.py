# Sending a motivational quote email on Tuesday

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

smtp_gmail = "smtp.gmail.com"
email_gmail = "garrettbeckerpython1@gmail.com"
password_gmail = "Pats1982!!"

smtp_yahoo = "smtp.mail.yahoo.com"
email_yahoo = "garrettbeckerpython1@yahoo.com"
password_yahoo = "manbmqmvtzykfvgt!!"

# Datetime module
import datetime as dt

# Sending a motivational quote email on Tuesday
quotes_list = []
quotes_file = open("quotes.txt", "r")
quotes_list = quotes_file.readlines()
quotes_list = [line.rstrip() for line in quotes_list]
quotes_file.close()

now = dt.datetime.now()
day_of_week = now.weekday()
random_quote = random.choice(quotes_list)

# Monday = 0, Sunday = 6
if day_of_week == 1:
    with smtplib.SMTP(smtp_yahoo) as connection:
        connection.starttls() # secures the connection
        connection.login(user=email_yahoo, password=password_yahoo)
        connection.sendmail(from_addr=email_yahoo, to_addrs=email_gmail, msg=f"Subject: Motivation!\n\n{random_quote}")

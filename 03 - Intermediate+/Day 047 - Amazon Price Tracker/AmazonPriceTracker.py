# 100 Days of Code: Python
# June 2, 2022
# Get notifications when an Amazon item gets cheaper

# Import modules
from bs4 import BeautifulSoup
import requests
import smtplib
from decouple import config

'''
Site to get HTTP header info for request
http://myhttpheader.com/
'''

# Email info
smtp_gmail = config("smtp_gmail")
email_gmail = config("email_gmail")
password_gmail = config("password_gmail")

# Webscrape to get the current price on Amazon
amazon_url = "https://www.amazon.com/LEGO-Starship-Building-Awesome-Pieces/dp/B08YP8HGLV/ref=sr_1_8?keywords=lego+dark+trooper+attack&qid=1654191957&s=toys-and-games&sprefix=lego+dark+%2Ctoys-and-games%2C176&sr=1-8"
price_target = 50.00

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(amazon_url, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

price_current = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
print(price_current)

# Compare price to target and send email if price is lower
is_lower = price_current < price_target
if is_lower:
    with smtplib.SMTP(smtp_gmail) as connection:
        connection.starttls() # secures the connection
        connection.login(user=email_gmail, password=password_gmail)
        connection.sendmail(
            from_addr=email_gmail,
            to_addrs=email_gmail,
            msg=f"Subject: Amazon Price Alert!\n\nPrice is now ${price_current} which is lower than your target of ${price_target}!\n{amazon_url}"
        )
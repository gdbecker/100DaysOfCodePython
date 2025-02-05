# 100 Days of Code: Python
# May 27, 2022
# Send stock alerts and news articles for specific stocks

# Import modules
from datetime import datetime
from datetime import timedelta
import requests
from twilio.rest import Client
from decouple import config

# Alpha Vantage stocks API info
av_key = config("av_key")

# News API info
news_key = config("news_key")

# Twilio info
twilio_account_sid = config("twilio_account_sid")
twilio_auth_token = config("twilio_auth_token")

# Get day info
now = datetime.today()
now_year = now.year
now_month = now.month
now_day = now.day
now_day_of_week = now.weekday()
today = f"{now_year}-{now_month:02d}-{now_day:02d}"

if now_day_of_week == 0:
    yesterday_datetime = now - timedelta(days=4)
    day_before_datetime = now - timedelta(days=5)
else:
    yesterday_datetime = now - timedelta(days=1)
    day_before_datetime = now - timedelta(days=2)

yesterday_year = yesterday_datetime.year
yesterday_month = yesterday_datetime.month
yesterday_day = yesterday_datetime.day
yesterday = f"{yesterday_year}-{yesterday_month:02d}-{yesterday_day:02d}"

day_before_year = day_before_datetime.year
day_before_month = day_before_datetime.month
day_before_day = day_before_datetime.day
day_before = f"{day_before_year}-{day_before_month:02d}-{day_before_day:02d}"

# ONE: get stock information from Alpha Vantage
stock = "TSLA"
av_url = "https://www.alphavantage.co/query"
av_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": stock,
    "interval": "60min",
    "apikey": av_url
}
response = requests.get(av_url, params=av_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (60min)"]

yesterday_data = stock_data[f"{yesterday} 19:00:00"]
day_before_data = stock_data[f"{day_before} 19:00:00"]

yesterday_close = round(float(yesterday_data["4. close"]),2)
day_before_close = round(float(day_before_data["4. close"]),2)

dollar_diff = yesterday_close - day_before_close
percent_diff = round((dollar_diff / day_before_close) * 100,2)

if percent_diff > 0:
    percent_diff_with_symbol = f"▲{percent_diff}%"
elif percent_diff < 0:
    percent_diff_with_symbol = f"▼{percent_diff}%"

# TWO: get news articles related to the stock
news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": stock,
    "apiKey": news_key
}
response = requests.get(news_url, params=news_parameters)
response.raise_for_status()
news_data = response.json()["articles"]
print(news_data)

most_recent_date = day_before_datetime
for article in news_data:
    if datetime.strptime(article["publishedAt"][0:10], "%Y-%m-%d") >= most_recent_date:
        headline = article["title"]
        briefly = article["description"]
        url = article["url"]


article_body = f'''
{stock}: {percent_diff_with_symbol}
Headline: {headline}
Briefly: {briefly}
Link: {url}
'''

# THREE: Send a text alert about the interested stock
client = Client(twilio_account_sid, twilio_auth_token)
message = client.messages \
    .create(
    body=article_body,
    from_="+18775409717",
    to="+19198961843"
)
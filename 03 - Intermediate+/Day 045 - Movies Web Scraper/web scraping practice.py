# Import modules
from bs4 import BeautifulSoup
import lxml
import requests

# Practice web scraping below
# Load in website data
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
title = soup.title.string

# Get all of a specific tag
all_anchor_tags = soup.findAll(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

# Find something specific
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Get a specific a tag link
company_url = soup.select_one(selector="p a").get("href")
print(company_url)

# Scrape a live website
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.findAll(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

# Get article with max number of upvotes
max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)
max_article = article_texts[max_index]
max_link = article_links[max_index]
print(max_article, max_link, max_upvotes)
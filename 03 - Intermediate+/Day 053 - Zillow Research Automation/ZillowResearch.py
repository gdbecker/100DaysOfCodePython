# 100 Days of Code: Python
# June 14, 2022
# Capstone: research apartments for rent in SF and record
# Using Selenium webdriver, BeautifulSoup, Google Forms

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import random

# Heads Up
print(
  "Visit https://docs.google.com/spreadsheets/d/1rnMr7qeuSRhTWpF8JPB15X95Dy0dNhgWsFYsiXqMKJU/edit#gid=1822230812 to see the results!"
)

# Constants
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
ZILLOW_HEADERS = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.9"
}
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeUX36nHhFG2rbIsYHYrKsXi6sZMLniAgxOwY7jaL8zlScA4Q/viewform"

# Get all apartment results (well, as many as you can b/c Zillow doesn't want bots lol)
response = requests.get(ZILLOW_URL, headers=ZILLOW_HEADERS)
wp = response.text
soup = BeautifulSoup(wp, "html.parser")

data = soup.findAll(name="ul",
                    class_="photo-cards photo-cards_wow photo-cards_short")
address_list = []
price_list = []
link_list = []

for article in soup.select(selector="ul li article"):
  for anchor in article.findAll(name="a"):
    link_list.append(anchor.get("href"))
    for address in anchor.findAll(name="address"):
      address_list.append(address.getText())
  price_list.append(
    article.find("span", {
      "data-test": "property-card-price"
    }).text.strip())

# Remove possible duplicates from these lists
address_list = list(dict.fromkeys(address_list))
price_list = list(dict.fromkeys(price_list))
link_list = list(dict.fromkeys(link_list))

print(price_list)

# Add results to Google Form with Selenium
# Set up driver
# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL)
driver.implicitly_wait(10)
time.sleep(2)

# Fill out Google Form for as many apartment results you have
for n in range(len(address_list)):
  address_field = driver.find_element(
    By.CSS_SELECTOR,
    "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
  )
  address_field.send_keys(address_list[n])

  price_field = driver.find_element(
    By.CSS_SELECTOR,
    "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
  )
  price_field.send_keys(price_list[n])

  link_field = driver.find_element(
    By.CSS_SELECTOR,
    "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
  )
  link_field.send_keys(link_list[n])

  submit_button = driver.find_element(
    By.CSS_SELECTOR,
    "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div"
  )
  submit_button.click()

  driver.implicitly_wait(10)
  time.sleep(random.randint(2, 4))

  submit_another_button = driver.find_element(
    By.CSS_SELECTOR,
    "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a"
  )
  submit_another_button.click()

  driver.implicitly_wait(10)
  time.sleep(random.randint(2, 4))

# Link to final Google Sheet with results
# https://docs.google.com/spreadsheets/d/1rnMr7qeuSRhTWpF8JPB15X95Dy0dNhgWsFYsiXqMKJU/edit?usp=sharing
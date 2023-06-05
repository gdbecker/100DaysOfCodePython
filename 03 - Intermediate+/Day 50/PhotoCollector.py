# 100 Days of Code: Python
# Agusut 22, 2022
# Collect 5 photos from Unplash based on user input
# Using Selenium webdriver

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import random

# Constants
SERV_WINDOWS = Service(r"/chromedriver_windows.exe")
SERV_MAC = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
UNPLASH_URL = "https://unsplash.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Ask user what they want to search for
search = input("What pics would you like? ")

# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)
driver.get(UNPLASH_URL)
driver.implicitly_wait(10)
time.sleep(random.randint(2, 4))

# Input search into Unplash
input_field = driver.find_element(By.CSS_SELECTOR, "#app > div > header > nav > div.hzGh7 > form > div.ejG8W.kypwe > input")
input_field.send_keys(search)
input_field.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
time.sleep(random.randint(2, 4))

# Get first 5 results
response = requests.get(str(driver.current_url), headers=HEADERS)
wp = response.text
soup = BeautifulSoup(wp, "html.parser")
images = soup.findAll(name="img", class_="YVj9w", itemprop="thumbnailUrl")[:5]
images_urls = []

for i in images:
    images_urls.append(i["src"])

# Save images to this folder
x = 1
for i in images_urls:
    image_data = requests.get(i).content
    with open(f'image{x}.jpg', 'wb') as file:
        file.write(image_data)
    x += 1
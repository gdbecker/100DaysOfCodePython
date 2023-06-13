# 100 Days of Code: Python
# Agusut 22, 2022
# Collect daily thoughts, jokes, random facts and journal prompts for teachers
# Using Selenium webdriver, BeautifulSoup, Google Forms

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
TEACHER_URL = "https://www.beagreatteacher.com/daily-fun-fact/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSep-Yo9CHHsaVLnRXVNQAP8VR--dcwHd4BxbTnETD9rQi9kzA/viewform?usp=sf_link"

# Get info from fun teacher site
response = requests.get(TEACHER_URL, headers=HEADERS)
wp = response.text
soup = BeautifulSoup(wp, "html.parser")

# Get the date
date = soup.find(name="a", rel="bookmark").text.split("–")[1].lstrip()

# Get thought of the dat
thought = soup.findAll(name="p")[1].text

# Get joke of the day
joke = soup.findAll(name="p")[2].text

# Get random fact of the day
fact = soup.findAll(name="p")[3].text

# Get journal prompt of the day
journal = soup.findAll(name="p")[4].text

# Add results to Google Form with Selenium
# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)
driver.get(GOOGLE_FORM_URL)
driver.implicitly_wait(10)
time.sleep(2)

# Fill out Google form and submit for the day's info
date_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
date_field.send_keys(date)

thought_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
thought_field.send_keys(thought)

joke_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
joke_field.send_keys(joke)

fact_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
fact_field.send_keys(fact)

journal_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
journal_field.send_keys(journal)

submit_button = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")
submit_button.click()

driver.implicitly_wait(10)
time.sleep(random.randint(2, 4))

# Link to final Google Sheet with results
# https://docs.google.com/spreadsheets/d/16Ai7SoxJW1Lqqi5v475awZCUV4n87cecwHZocMcpLHY/edit?resourcekey#gid=1074284983
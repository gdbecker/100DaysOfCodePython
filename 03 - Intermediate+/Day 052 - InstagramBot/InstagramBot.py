# 100 Days of Code: Python
# June 14, 2022
# Instagram bot to follow all the followers/who they're following of chosen account
# Using Selenium webdriver

# IT WORKS!

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from decouple import config

# Constants
SERV_WINDOWS = Service(r"/chromedriver_windows.exe")
SERV_MAC = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
INSTA_EMAIL = config("INSTA_EMAIL")
INSTA_PASSWORD = config("INSTA_PASSWORD")
INSTA_HANDLE = config("INSTA_HANDLE")
ACCOUNT = "nasaearth"
LOGIN_URL = "https://www.instagram.com"
ACCOUNT_URL = f"{LOGIN_URL}/{ACCOUNT}/following/"

# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)

# Log into Instagram
driver.get(LOGIN_URL)
driver.implicitly_wait(10)
time.sleep(2)

email_field = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
email_field.send_keys(INSTA_EMAIL)
password_field = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
password_field.send_keys(INSTA_PASSWORD)
password_field.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
time.sleep(10)

# Go to chosen account page and click on their "following" list (since this is shorter)
driver.get(ACCOUNT_URL)

# Follow all the accounts on the list
fBody = driver.find_element(By.XPATH, "//div[@class='_aano']")
scroll = 0
while scroll < 7: # scroll 7 times, make sure to go to the bottom (depends on list length)
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(2)
    scroll += 1

fList = driver.find_elements(By.CSS_SELECTOR, "li button")

for f in fList:
    f.click()
    time.sleep(2)
# 100 Days of Code: Python
# June 3, 2022
# Automatically click the cookie with a bot
# Using Selenium webdriver

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
serv = Service(r"C:\Users\garrett.becker\OneDrive - Elliott Davis LLP\Documents\Udemy - Python 100 Days of Code\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# Get the cookie button ready
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(By.CSS_SELECTOR, "#cookie")

# Click for 5 minutes, and check for every five seconds
timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    cookie_button.click()
    if time.time() > timeout:
        upgrade_buttons = driver.find_elements(By.CSS_SELECTOR, "div[class=''] b")
        upgrade_buttons[-1].click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_rate = driver.find_element(By.CSS_SELECTOR, "#cps").text
        print(cookie_rate)
        driver.quit()
        break

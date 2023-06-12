# 100 Days of Code: Python
# June 4-5, 2022
# Automatically apply for jobs on LinkedIn
# Using Selenium webdriver

# Stopping because it's not working correctly, and the App Brewery job posting is gone
# I won't need to be using this much anyway

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
serv_windows = Service(r"/chromedriver_windows.exe")
serv_mac = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
driver = webdriver.Chrome(service=serv_windows)

driver.get("https://www.linkedin.com/jobs/?showJobAlertsModal=false")
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email = driver.find_element(By.CSS_SELECTOR, "#username")
email.send_keys("")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("")

# For some reason it doesn't want to click on the final button to sign in :(
# sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
# sign_in_btn.click()

# driver.quit()
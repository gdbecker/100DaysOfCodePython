# 100 Days of Code: Python
# August 6, 2022
# Custom automation app
# Automatically add books to my "to-read" list on Goodreads.com

# IT WORKS!
# Big key was to update the chromedriver to match the updated Chrome I had

'''
In the books_to_read.csv file, put author name first and then book title as specific as needed.
Can sometimes include the series name after book title and ## in the series.
'''

# Import modules
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas

# Constants
SERV_WINDOWS = Service(r"/chromedriver_windows.exe")
SERV_MAC = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
GOODREADS_EMAIL = "garrettdbecker@gmail.com"
GOODREADS_PASSWORD = "dbldkr123!!"

# Get list of books to add
raw_data = pandas.read_csv("books_to_read.csv")
raw_books = raw_data["Books"].to_dict()
books_list = list(raw_books.values())

# Set up list for Goodreads result - was it added or not added?
search_results = []

# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)

# Log into goodreads.com
driver.get("https://www.goodreads.com/")
driver.implicitly_wait(10)
time.sleep(2)

amazon_btn = driver.find_element(By.CSS_SELECTOR, "a.gr-button.gr-button--amazon.gr-button--fullWidth.gr-button--auth")
amazon_btn.click()

driver.implicitly_wait(10)
time.sleep(2)

email_field = driver.find_element(By.CSS_SELECTOR, "#ap_email")
email_field.send_keys(GOODREADS_EMAIL)

password_field = driver.find_element(By.CSS_SELECTOR, "#ap_password")
password_field.send_keys(GOODREADS_PASSWORD)

sign_in_btn = driver.find_element(By.CSS_SELECTOR, "#signInSubmit")
sign_in_btn.click()

driver.implicitly_wait(10)
time.sleep(2)

# Search for each book and add to my to-read list
for book in books_list:
    driver.implicitly_wait(10)
    time.sleep(2)

    search_bar = driver.find_element(By.CSS_SELECTOR, "input.searchBox__input.searchBox__input--navbar")
    search_bar.send_keys(book)
    search_bar.send_keys(Keys.ENTER)

    driver.implicitly_wait(10)
    time.sleep(2)

    try:
        read_btn = driver.find_element(By.CSS_SELECTOR, "span.progressTrigger")
        read_btn.click()

        driver.implicitly_wait(10)
        time.sleep(2)

        search_results.append("Added")
    except:
        search_results.append("Not added")

    goodreads_btn = driver.find_element(By.CSS_SELECTOR, "a.siteHeader__logo")
    goodreads_btn.click()

# Save books and search results to a new .csv
with open("goodreads_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(zip(books_list, search_results))
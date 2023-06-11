# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome driver
serv = Service(r"C:\Users\garrett.becker\OneDrive - Elliott Davis LLP\Documents\Udemy - Python 100 Days of Code\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# # Getting number of articles from Wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# num_articles = driver.find_elements(By.CSS_SELECTOR, "#articlecount > a")[0]

# # Practice clicking
# all_portals = driver.find_element(By.LINK_TEXT, "Contents")
# # all_portals.click()
#
# # Automatically type
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Practice using Angela's App Brewery site
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("First")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Last")
email = driver.find_element(By.NAME, "email")
email.send_keys("example@mail.com")
submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
submit.click()
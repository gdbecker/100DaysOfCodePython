# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Chrome driver
serv = Service(r"C:\Users\garrett.becker\OneDrive - Elliott Davis LLP\Documents\Udemy - Python 100 Days of Code\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# Practice grabbing HTML elements
# Amazon price tracker from day 47
# driver.get("https://www.amazon.com/LEGO-Starship-Building-Awesome-Pieces/dp/B08YP8HGLV/ref=sr_1_8?keywords=lego+dark+trooper+attack&qid=1654191957&s=toys-and-games&sprefix=lego+dark+%2Ctoys-and-games%2C176&sr=1-8")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute("innerHTML"))

# Getting upcoming dates from python.org
driver.get("https://www.python.org/")
dates = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")
events = {}

for x in range(len(event_names)):
    events[x] = {
        "time": dates[x].get_attribute("datetime").split("T")[0],
        "name": event_names[x].text
    }

print(events)

driver.quit()
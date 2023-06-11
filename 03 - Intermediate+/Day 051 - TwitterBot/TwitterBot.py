# 100 Days of Code: Python
# June 6 & 13, 2022
# Twitter complaining bot when internet speed is too low
# Using Selenium webdriver

# IT WORKS!

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Constants
PROMISED_DOWN = 150
PROMISED_UP = 10
SERV_WINDOWS = Service(r"/chromedriver_windows.exe")
SERV_MAC = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
TWITTER_HANDLE = "gbpython11"
TWITTER_EMAIL = "garrettbeckerpython1@yahoo.com"
TWITTER_PASSWORD = "Pats1982!!"

# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)

# Get current internet speed
driver.get("https://www.speedtest.net/")

driver.implicitly_wait(10)
time.sleep(2)

go_button = driver.find_element(By.CSS_SELECTOR, ".js-start-test.test-mode-multi")
go_button.click()

time.sleep(80)

download_speed = float(driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed").text)
upload_speed = float(driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed").text)

# Check if speeds are lower than guaranteed
tweet = "Hey Internet Provider! "
low_download_speed = download_speed < PROMISED_DOWN
low_upload_speed = upload_speed < PROMISED_UP

if low_download_speed:
    tweet += f" Why is my download speed {download_speed}Mbps when you promised {PROMISED_DOWN}Mbps? "

if low_upload_speed:
    tweet += f" Why is my upload speed {upload_speed}Mbps when you promised {PROMISED_UP}Mbps? "

if not low_download_speed and not low_upload_speed:
    tweet += " You're doing great!"

# Send tweet
# Logging in
driver.get("https://twitter.com/")

driver.implicitly_wait(10)
time.sleep(2)

sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
#sign_in_btn = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
sign_in_btn.click()

driver.implicitly_wait(10)
time.sleep(2)

email_field = driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')
email_field.send_keys(TWITTER_EMAIL)

driver.implicitly_wait(10)
time.sleep(2)

email_field.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
time.sleep(2)

# In case Twitter asks for phone number or handle:
try:
    verify_field = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
    time.sleep(2)
    verify_field.send_keys(TWITTER_HANDLE)
    driver.implicitly_wait(10)
    time.sleep(2)
    verify_field.send_keys(Keys.ENTER)
except:
    pass

password_field = driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input')
password_field.send_keys(TWITTER_PASSWORD)

driver.implicitly_wait(10)
time.sleep(2)

password_field.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
time.sleep(2)

# Typing and sending tweet
tweet_field = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
tweet_field.send_keys(tweet)

driver.implicitly_wait(10)
time.sleep(2)

tweet_btn = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
tweet_btn.click()

driver.implicitly_wait(10)
time.sleep(2)
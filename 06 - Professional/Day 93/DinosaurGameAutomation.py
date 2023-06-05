# 100 Days of Code: Python
# July 27, 2022
# Automates playing the Google dinosaur game

# Import modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import PIL
import pyautogui

# Constants
SERV_WINDOWS = Service(r"/chromedriver_windows.exe")
SERV_MAC = Service(r"/Volumes/GoogleDrive/My Drive/Jobs and Career/Udemy Courses/100 Days of Code Python Bootcamp/chromedriver_mac.exe")
x_jump = 437
y_jump_1 = 568
y_jump_2 = 570

# Set up driver
driver = webdriver.Chrome(service=SERV_WINDOWS)

# Access dino site
driver.get("https://elgoog.im/t-rex/")

driver.implicitly_wait(6)
time.sleep(2)

# Start game
pyautogui.press("up")

# Dino jump before cactus
while True:
    im = pyautogui.screenshot()
    if im.getpixel((x_jump, y_jump_1)) != (247, 247, 247) or im.getpixel((x_jump, y_jump_2)) != (247, 247, 247):
        pyautogui.press("up")

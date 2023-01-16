import time

from selenium import webdriver
from selenium.webdriver.common.by import By

""" UPLOADING FILE"""

browser = webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/upload")

# METHOD-1
browser.save_screenshot("Pavan.png")

# METHOD - 2
browser.get_screenshot_as_file("D:\Screenshot\SS\Screenshot.png")


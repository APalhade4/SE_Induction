import time
from selenium import webdriver
from selenium.webdriver.common.by import By as abc

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(15)
# This time is provided by Python.
# why Time.sleep = It will hold the page for give time.
# It will hold the page for particular element.
# If given argument is not correct then it will throw the error instantly.

driver.implicitly_wait(120)
# This time is provided by Selenium.
# why implicitly_wait = It will hold the page for give time.
# It will hold the page for Every element.
# If given argument is not correct then it will throw the error after given time slot.


''' Explicit Wait '''
# This time is provided by External class.
# We need to Import 2 classes for using this time.
# It is only applicable to particular element.
# In this wait we are providing the Explicit wait for particular element.














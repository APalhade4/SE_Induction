

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

text = driver.find_element(By.ID, "myTextarea")
text.send_keys("Hello Ambition \nWe are learning python \n with Mr. Anurag")

time.sleep(15)
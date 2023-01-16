import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

# Method -1 for Sending Keys
text = driver.find_element(By.ID, "myTextInput")
text.send_keys("Hello Ambition")


# Method -2 for Sending Keys
text = driver.find_element(By.ID, "myTextInput").send_keys("Hello Ambition")



time.sleep(15)




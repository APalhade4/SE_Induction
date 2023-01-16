from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

placeholder = driver.find_element(By.ID, "placeholderText")
placeholder_2 = placeholder.get_attribute("placeholder")
print(placeholder_2)
placeholder.send_keys("Hello Shantanu")


time.sleep(15)
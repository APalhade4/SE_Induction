from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

paragraph_text = driver.find_element(By.ID, "pText").text
print(paragraph_text)

time.sleep(15)





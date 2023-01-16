import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

checkbox = driver.find_element(By.ID, "checkBox4")
checkbox.click()  # -----------------------------------> Checking checkbox
time.sleep(5)
checkbox.click()  # -----------------------------------> Un-checking checkbox


time.sleep(15)












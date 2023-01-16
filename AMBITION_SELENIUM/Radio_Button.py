import time

from selenium import webdriver
from selenium.webdriver.common.by import By


swapnil = webdriver.Chrome()
swapnil.get("https://seleniumbase.io/demo_page")

# swapnil.find_element(By.ID, "radioButton1").click()
# time.sleep(5)
# swapnil.find_element(By.ID, "radioButton2").click()
# time.sleep(5)
# swapnil.find_element(By.ID, "radioButton1").click()
# time.sleep(5)
# swapnil.find_element(By.ID, "radioButton2").click()

radio_1 = swapnil.find_element(By.ID, "radioButton1")
radio_1.click()

radio_2 = swapnil.find_element(By.ID, "radioButton2")
radio_2.click()


time.sleep(15)








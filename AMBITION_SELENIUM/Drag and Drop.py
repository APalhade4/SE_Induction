import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/drag_drop.html")

Target_Debit_Amount = driver.find_element(By.CSS_SELECTOR, '#amt7 > li')
Source_Debit_5000 = driver.find_element(By.XPATH, '//*[@id="fourth"]/a')

# action = ActionChains(webdriver.Chrome())
action = ActionChains(driver)

time.sleep(5)
drag_drop = action.drag_and_drop(Source_Debit_5000, Target_Debit_Amount).perform()
time.sleep(10)








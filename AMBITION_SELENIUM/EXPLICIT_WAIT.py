

# CSS Selector : CSS stands for Cascading Style Sheet
# Why we are using CSS Selector:
    # CSS selector mainly use the character sequence pattern which identifies the web element on HTML page.
    # CSS selector has been used by Front-End developer to locate the web element on web-page.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
remove_button.click()
WebDriverWait(driver, 50).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="message"]')))
text = driver.find_element(By.XPATH, '//*[@id="message"]')
print(text.text)



# add_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
# add_button.click()
# WebDriverWait(driver, 50).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
# text_1 = driver.find_element(By.XPATH, '//*[@id="message"]')
# print(text_1.text)

enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
enable_button.click()

# WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, 'message')))
# text_3 = driver.find_element(By.ID, 'message')
# print(text_3.text)

WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
text_box = driver.find_element(By.XPATH, '//*[@id="input-example"]/input')
text_box.send_keys("Hello Explicit Wait")



time.sleep(10)
import time
from AMBITION_PYTEST import test_fixture
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

text = driver.find_element(By.ID, "myTextInput")
text.send_keys("Hello Ambition")

text_area = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[4]/textarea")
text_area.send_keys("Hello Ambition \nwe are learning \npython")

time.sleep(5)

driver.back()

time.sleep(5)

driver.forward()

time.sleep(5)

driver.maximize_window()

driver.refresh()

driver.minimize_window()


# How to handle Chrome window
# get
# find elements
# send keys
# locators
# close
# quit()
# back
# forward


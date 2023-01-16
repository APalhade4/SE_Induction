

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

# Method - 1 for reading Value
pre_filled_text = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input")
abc = pre_filled_text.get_attribute("value")
print(abc)


# Method - 2 for reading Value
pre_filled_text = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input").get_attribute("value")
print(pre_filled_text)


time.sleep(15)
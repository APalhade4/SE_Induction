
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

# drop_box = driver.find_element(By.ID, "mySelect")  #----> This is the Drop-Down


# drop_box_option.select_by_index(2)
# time.sleep(3)
# drop_box_option.select_by_value("50%")
# time.sleep(3)
# drop_box_option.select_by_visible_text("Set to 100%")

""" HOME WORK : Perform Deselect Method"""

drop_box = driver.find_element(By.ID, "mySelect")
drop_box_option = Select(drop_box)   # Object for Select Class


all_options = drop_box_option.options

for option in all_options:
    print(option.text)
print("Count of drop down list is: ", len(all_options))
time.sleep(15)












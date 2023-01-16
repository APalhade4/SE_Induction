

# What is Handle?
#         Unique ID for browser window

# 1. Current_Window_Handle
# 2. Window_handle
# 3. switch_to.windows(handle)

# Whenever we are performing the Windows handling that will perform for child parent relationship.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

# driver.maximize_window()
# driver.refresh()
# driver.minimize_window()

time.sleep(15)
driver.implicitly_wait(15)

page_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

page_2 = driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').click()

handle = driver.current_window_handle
print(handle)

# driver.implicitly_wait(150)

all_handle = driver.window_handles
for i in all_handle:
    print(i)

option1 = driver.window_handles[1]
option2 = driver.window_handles[2]
option0 = driver.window_handles[0]

driver.switch_to.window(option1)
driver.switch_to.window(option2)
driver.switch_to.window(option0)













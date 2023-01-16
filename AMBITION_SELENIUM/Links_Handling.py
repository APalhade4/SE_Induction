import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#
# driver.get("https://the-internet.herokuapp.com/windows")
#
# links = driver.find_elements(By.TAG_NAME, 'a')
# # print(links)
# for i in links:
#     print(i.text)
#     URL = i.get_attribute("href")
#     print(URL)




# ID
# NAME
# XPATH
# TAG_NAME
# Link_text
# pertial_link_text
#
# driver.get("https://the-internet.herokuapp.com/windows")

# all_links = driver.find_elements(By.TAG_NAME, 'a')
# print("Total number of links available is: ", len(all_links))
# for i in all_links:
#     print(i.text)

# link_1 = driver.find_element(By.LINK_TEXT, "Click Here for opening page")
# link_1.click()
# time.sleep(8)
#
# link_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Selen")
# link_2.click()
# time.sleep(8)



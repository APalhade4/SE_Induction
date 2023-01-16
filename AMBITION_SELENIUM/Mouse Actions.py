import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

""" To use the Action Chains, We must have to call Perform()"""


driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

hover = driver.find_element(By.ID, 'myDropdown')
hover_option_1 = driver.find_element(By.ID, 'dropOption1')
hover_option_2 = driver.find_element(By.ID, 'dropOption2')
hover_option_3 = driver.find_element(By.ID, 'dropOption3')
text_box = driver.find_element(By.XPATH, '//*[@id="myTextInput2"]')
color_button = driver.find_element(By.ID, 'myButton')

action = ActionChains(driver)

mouse_action_1 = action.move_to_element(hover).perform()
mouse_action_2 = action.move_to_element(hover_option_1).click().perform()
time.sleep(5)

Double_click = action.move_to_element(text_box).double_click().perform()
time.sleep(5)

Right_click = action.context_click(color_button).perform()
time.sleep(5)

checkbox = driver.find_element(By.ID, 'checkBox1')
checkbox.click()
drop_box_1 = driver.find_element(By.CSS_SELECTOR, '#drop1')
drop_box_2 = driver.find_element(By.CSS_SELECTOR, '#drop2')
time.sleep(5)
action = ActionChains(driver)
action.drag_and_drop(drop_box_1, drop_box_2).perform()
time.sleep(5)




#
#
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# a = driver.find_element(By.ID, "column-a")
# b = driver.find_element(By.ID, "column-b")
#
# action = ActionChains(driver)
#
# action.drag_and_drop(a, b).click().perform()
# time.sleep(5)


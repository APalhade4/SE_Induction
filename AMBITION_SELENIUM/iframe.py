from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.switch_to.frame("myFrame3")
check_box = driver.find_element(By.ID, "checkBox6").click()

time.sleep(5)

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
driver.switch_to.frame("iframeResult")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/button").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)











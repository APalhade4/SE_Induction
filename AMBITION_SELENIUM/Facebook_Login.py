import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get(input("Enter Your URL : "))

email = driver.find_element(By.NAME, "email")
email.send_keys(input("Enter Your User_Name : "))

password = driver.find_element(By.ID, "pass")
# xyz = input("Enter")
password.send_keys(input("Enter Your Password : "))

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
button.click()

time.sleep(15)


















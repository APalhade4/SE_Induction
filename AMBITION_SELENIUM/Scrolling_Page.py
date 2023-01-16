import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/seleniumbase/SeleniumBase")

# Scrolling by PIXELS
driver.execute_script("window.scrollBy(0, 2000)")

# Scrolling up to Element
jenkins = driver.find_element(By.XPATH, '//*[@id="readme"]/div[2]/article/p[47]/a[2]/img')
driver.execute_script("arguments[0].scrollIntoView();", jenkins)

# Scrolling up to End of Page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

# Scrolling to TOP of Page
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

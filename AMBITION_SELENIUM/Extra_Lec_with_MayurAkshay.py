from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

# Method - 1 for Clicking on button
button = driver.find_element(By.ID, "myButton").click()


# Method - 2 for Clicking on button
button = driver.find_element(By.ID, "myButton")
button.click()

time.sleep(15)


class LoginPage():

    def login(self):
        text_from_element = self.edtUserName.get_text()
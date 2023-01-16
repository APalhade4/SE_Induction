
import Utils
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
path = "D:\python\Key_Driven_testing.xlsx"
rows = Utils.get_no_rows(path, 'DDT')

for i in range(2, rows+1):
    username = Utils.read_data(path, 'DDT', i, 1)
    password = Utils.read_data(path, 'DDT', i, 2)
    email = driver.find_element(By.ID, "email")
    email.send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    if driver.title == "Facebook – log in or sign up":
        print("Test Case is Passed...")
        Utils.write_data(path, 'DDT', i, 3, "Passed")
    else:
        print("Test Case is Failed...")
        Utils.write_data(path, 'DDT', i, 3, "Failed")
    driver.find_element(By.LINK_TEXT, "m.facebook").click()



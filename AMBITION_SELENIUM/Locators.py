import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

actual_title = driver.title
print(actual_title)
Excpected_title = "Facebook – log in or sign up"

send_email = driver.find_element(By.ID, "email")
send_email.send_keys("9529658851")
send_password = driver.find_element(By.NAME, "pass")
send_password.send_keys("Swami@123")
click_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
click_button.click()

class Facebook:
    def facebook_login(self):
        if actual_title == Excpected_title:
            send_email = driver.find_element(By.ID, "email")
            send_email.send_keys("9529658851")
            send_password = driver.find_element(By.NAME, "pass")
            send_password.send_keys("Swami@123")
            click_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
            click_button.click()
        else:
            print("Program executed Unsuccessful")

obj_2 = Facebook()
obj_2.facebook_login()

time.sleep(8)




''' To find any elements we have a Locators '''

# ID -------------> It is a Fastest Locator, and It is unique.
# Name
# class name
# Tag ------------->
# Partiallink
# linktext
"Custom Locators"
# Xpath -------------> We are using most probably Xpath, When we dont have any
                     # Locator in code, that we are using XPATH.
# CSS Selector

'''================================================================================'''

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
#
# text = driver.find_element(By.ID, "myTextInput")
# text.send_keys("Hello Ambition")
#
# text_area = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[4]/textarea")
# text_area.send_keys("Hello Ambition \nwe are learning \npython")
#
# time.sleep(5)
#
# driver.back()
#
# time.sleep(5)
#
# driver.forward()
#
# time.sleep(5)


# How to handle Chrome window
# get
# find elements
# send keys
# locators
# close
# quit()
# back
# forward



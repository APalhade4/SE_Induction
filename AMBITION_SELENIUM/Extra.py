import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

chrome = webdriver.ChromeOptions()

# allow_or_block = ("profile.default_content_setting_values.notifications": 2) # 1 = Allow , 2 = Block
# chrome_option.add_experimental_option("prefs", allow_or_block)

allow_or_block = chrome.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1 })

driver = webdriver.Chrome(chrome_options=chrome, executable_path=r"C:\Users\Anurag Palhade\AppData\Local\Programs\Python\Python310\chromedriver.exe")

driver.get('https://www.facebook.com/')
# For email
send_email= driver.find_element(By.ID,'email')
send_email.send_keys('9529658851')

# For password
send_password= driver.find_element(By.NAME,'pass')
send_password.send_keys('Swami@123')

# Click login button
Click_login_button= driver.find_element(By.NAME,'login')
Click_login_button.click()

time.sleep(100)











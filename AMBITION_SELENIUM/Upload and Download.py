import time

from selenium import webdriver
from selenium.webdriver.common.by import By

""" UPLOADING FILE"""

browser = webdriver.Chrome()

browser.get("https://the-internet.herokuapp.com/upload")
choose_file = browser.find_element(By.XPATH, '//*[@id="file-upload"]')
choose_file.send_keys("D:\Screenshot\SS\Lambition.jpg.png")  # ------> File location from your computer
time.sleep(10)
upload_button = browser.find_element(By.XPATH, '//*[@id="file-submit"]')
upload_button.click()
time.sleep(15)




""" DOWNLOADING FILE"""


# browser.get("https://the-internet.herokuapp.com/download")
#
# time.sleep(5)
# file_name = browser.find_element(By.XPATH, '//*[@id="content"]/div/a[5]')
# file_name.click()
# time.sleep(10)


# browser.get("https://www.microsoft.com/en-in/microsoft-teams/download-app#desktopAppDownloadregion")
# time.sleep(5)
# teams = browser.find_element(By.XPATH, '//*[@id="office-DesktopAppDownload-wqkfqkk"]/div/div[2]/div[2]/div/div/a/span')
# teams.click()
# time.sleep(10)
#
#



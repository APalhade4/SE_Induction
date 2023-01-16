
# What is Table?
        # Combination of Rows and Columns

# tr = Table Row
# td = Table data  (Column)
# th = Table Header   (th always will be at TOP i.e., at first Row)

# From where we will get the data
    # 1. Excel
    # 2. SQL Server
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/tables")
#
# # Method - 1
# website = driver.find_element(By.XPATH, '//*[@id="table1"]/thead/tr/th[5]/span')
# print(website.text)
#
# # Method - 2
# print(driver.find_element(By.XPATH, '//*[@id="table1"]/tbody/tr[3]/td[3]').text)
#
# element = driver.find_element(By.XPATH, '//*[@id="table1"]/tbody/tr[2]/td[4]')
# print(element.text)
#
# element_1 = driver.find_element(By.XPATH, '//*[@id="table1"]/tbody/tr/th[4]')
# print("Fourth Header is : ",element_1.text)


driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")

driver.execute_script("window.scrollBy(0, 3150)")

time.sleep(5)

row = driver.find_element(By.XPATH, '//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr[1]/th[3]')
print(row.text)

row = driver.find_elements(By.XPATH, '//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr[1]/th')
for i in row:
    print(i.text)

row = driver.find_elements(By.XPATH, '//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr[2]/td')
for i in row:
    print(i.text)

# row = driver.find_elements(By.XPATH, '//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr/td')
# columns = driver.find_elements(By.XPATH, '//*[@id="post-1688"]/div/div[1]/form/table/tbody/tr/td[2]')
# for i in row:
#     print(i.text, end=' ')
#     for j in columns:
#         print(j.text, end = ' ')

time.sleep(10)


''' Assignment '''

# print rows and columns using only one for loop?








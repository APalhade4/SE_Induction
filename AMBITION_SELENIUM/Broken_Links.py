

'''=============================================================================================
        HOW TO FIND BROKEN LINKS (API TESTING QUESTION)
============================================================================================='''

'''                 " SQL "                               "API"       '''

''' GET ------> (SELECT) ---------------------------> Receive/Read/Display'''
''' POST -----> (Creating New Record--> INSERT) -----> INSERTNG'''
''' PUT -----> (UPDATE Existing Record) -------------> UPDATING'''
''' DELETE -----> (DELETE Existing Record) ----------> DELETING'''
''' PATCH -----> (UPDATE Existing Record) ------------> UPDATING'''

''' Example of JSON FILE/FORMAT: '''

# {
#     "Your_Name" :
#         [
#             "Anurag", "Akshay", "Pooja", "Suraj"
#         ],
#     "Education" : "BE",
#     "Passout" : "2021"
# }

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

all_links = driver.find_elements(By.TAG_NAME, 'a')
print("Total number of links available on page is : ", len(all_links))

for links in all_links:
    # print(links.text)
    URL = links.get_attribute("href")
    # print(URL)
    Result = requests.head(URL)
    # print(Result)
    # print(URL, Result)
    # print(URL, Result.status_code)
    if Result.status_code != 200:
        print(URL, Result.status_code)


# 200 - OK
# 401
# 403
# 404
# 303
# 301


# Every HTTP request or response have a Header file.
# What is header?
        # Header is a data packet that carries metadata or
        # other information which is necessary for processing the main data.

# What is Broken Link?
        # The link which is not opening due to some reasons that link is called as Broken Link.

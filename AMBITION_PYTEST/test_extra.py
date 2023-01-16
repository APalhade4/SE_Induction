import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_fb_login_chrome_001():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("9529658851")
    password = driver.find_element(By.ID, "pass")
    password.send_keys("Swami@123")
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    button.click()
    assert True


def test_fb_chrome_002():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("9529658851")
    password = driver.find_element(By.ID, "pass")
    password.send_keys("Swami@123")
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    button.click()
    assert True


def test_fb_login_003():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("9529658851")
    password = driver.find_element(By.ID, "pass")
    password.send_keys("Swami@123")
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    button.click()
    assert True

time.sleep(15)
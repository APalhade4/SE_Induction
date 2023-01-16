import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")


# alert_button = driver.find_element(By.ID, "alertButton").click()
# driver.switch_to.alert.accept()       # -----------> OK

# time_alert_button = driver.find_element(By.ID, "timerAlertButton")  # ---> Here we need to use Implicit or Explicit waits
# time_alert_button.click()
# time.sleep(6)
time_alert_button = WebDriverWait(driver, 25).until(EC.presence_of_element_located(By.ID, "timerAlertButton"))

driver.switch_to.alert.accept()

# alert_button = driver.find_element(By.ID, "promtButton").click()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()        # ------------> Cancel







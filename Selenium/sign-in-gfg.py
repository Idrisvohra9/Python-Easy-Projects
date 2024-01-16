import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")

time.sleep(8)

btn = driver.find_element(By.XPATH, "//*[@id='userProfileId']/a")
btn.click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='luser']").send_keys("idrishaider987@gmail.com")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("idrisdgr8")
driver.find_element(By.XPATH, "/html/body/div[8]/div[3]/div/div[2]/div[1]/section[1]/form/button").click()


time.sleep(20)
driver.close()
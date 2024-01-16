import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/phpmyadmin/index.php?route=/")
driver.find_element(By.XPATH, "//*[@id='themeSelect']/option[2]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='themeSelect']/option[3]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='themeSelect']/option[4]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='themeSelect']/option[5]").click()

driver.fullscreen_window()

time.sleep(10)
driver.close()
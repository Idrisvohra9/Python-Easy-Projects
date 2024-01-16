import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.maximize_window()

driver.get('https://demoqa.com/buttons')
time.sleep(15)

# Double click:
dblClick = driver.find_element(By.ID, 'doubleClickBtn')
action.double_click(dblClick).perform()

# Right click:
rightClick = driver.find_element(By.ID, "rightClickBtn")
action.context_click(rightClick).perform()

time.sleep(15)

driver.close()

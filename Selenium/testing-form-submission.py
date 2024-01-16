import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationintesting.online/")

new_title = "Website under Automation - Idris Vohra"

console = driver.execute_script(f"document.title = '{new_title}'")
name = "Idris"
email = "idris@gmail.com"
phone = "1234561111111"
subject = "Issuing an Inquiry"
msg = "Lol, SOme DescRiptIon"

time.sleep(2)

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "phone").send_keys(phone)
driver.find_element(By.ID, "subject").send_keys(subject)
driver.find_element(By.ID, "description").send_keys(msg)
driver.find_element(By.ID, "submitContact").click()

time.sleep(10)
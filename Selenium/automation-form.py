import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# For making the html page load faster:
options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)
website = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"

driver.maximize_window()
driver.get(website)
input_elements = driver.find_elements(By.TAG_NAME, "input")
# print(input_elements)
# print(len(input_elements))
input_values = ["Idris", "Vohra"]
i = 0
for element in input_elements:
  element.send_keys(input_values[i])
  i+=1
  
# driver.implicitly_wait(120)  # Waits for 10 seconds
time.sleep(100)
# driver.quit()
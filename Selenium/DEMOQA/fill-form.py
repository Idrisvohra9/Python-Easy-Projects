import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.ID,'firstName').send_keys('Aryan')
driver.find_element(By.ID,'lastName').send_keys('Sharma')
driver.find_element(By.ID,'userEmail').send_keys('Aryan@gmail.com')
driver.find_element(By.XPATH,"//*[@id='genterWrapper']/div[2]/div[1]/label").click()
driver.find_element(By.ID,"userNumber").send_keys('7016977853')
date_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dateOfBirthInput']")))

# Clear the content of the date field using JavaScript
driver.execute_script("arguments[0].value = '';", date_field)
# driver.find_element(By.ID,"dateOfBirthInput").send_keys('1 Jan 2024')
# driver.find_element(By.XPATH,"//*[@id='subjectsContainer']/div/div[1]").send_keys('English')
# driver.find_element(By.XPATH,"//*[@id='hobbiesWrapper']/div[2]/div[1]/label").click()
driver.find_element(By.ID,"uploadPicture").send_keys(f"/mnt/Programming/Python/Python-Easy-Projects/Selenium/DEMOQA/tiger-bhai.jpg")
driver.find_element(By.ID,"currentAddress").send_keys("Ahmedabad")
# driver.find_element(By.XPATH,"//*[@id='state']/div/div[2]/div").click()
element_to_hide = driver.find_element(By.CSS_SELECTOR,"#fixedban")
driver.execute_script("arguments[0].style.display='none';", element_to_hide)

element_to_hide2 = driver.find_element(By.CSS_SELECTOR,"#app > footer")
driver.execute_script("arguments[0].style.display='none';", element_to_hide2)

driver.execute_script("window.scrollBy(0, 1500);")
driver.find_element(By.ID,"submit").click()


time.sleep(5)

driver.close()
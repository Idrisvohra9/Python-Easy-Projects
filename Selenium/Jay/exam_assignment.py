from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the driver
driver = webdriver.Chrome()

# Navigate to the Sauce Labs demo website
print("Navigating to the Sauce Labs demo website...")
driver.get("https://www.saucedemo.com/")

# Find the username and password fields using their XPaths
print("Locating the username and password fields...")
username = driver.find_element(By.XPATH, "//input[@name='user-name']")
password = driver.find_element(By.XPATH, "//input[@name='password']")

# Enter credentials and submit the login form
print("Entering credentials and logging in...")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
password.send_keys(Keys.RETURN)
time.sleep(1)

# Sort the products by price
print("Sorting the products by price...")
driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[3]").click()
time.sleep(2)

# Add a product to the cart
print("Adding a product to the cart...")
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
time.sleep(2)

# Proceed to checkout
print("Proceeding to checkout...")
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
time.sleep(2)

# Fill out the checkout form
print("Filling out the checkout form...")
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Idris")
driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Vohra")
driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("12345")

time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='continue']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='finish']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()
time.sleep(1)

# Close the browser window
print("Test completed. Closing the browser window.")
driver.quit()

# import module
from selenium import webdriver

# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Chrome(r"C:\\bin\\chromedriver.exe")

# get https://www.geeksforgeeks.org/
driver.get("https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/")

# Maximize the window and let code stall

driver.maximize_window()


# Obtain button by link text and click.
button = driver.find_element_by_link_text("Python")
button.click()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.maximize_window()

search = driver.find_element("name", "search_query")

search.send_keys("Dream")

search.send_keys(Keys.ENTER)
time.sleep(5)

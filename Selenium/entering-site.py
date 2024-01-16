from selenium import webdriver
driver = webdriver.Chrome()
# Navigate to the desired website
website_url = 'https://youtube.com'  # Replace this with the URL of the website you want to open
driver.get(website_url)
driver.maximize_window()

# Wait for some time (optional)
driver.implicitly_wait(120)  # Waits for 10 seconds


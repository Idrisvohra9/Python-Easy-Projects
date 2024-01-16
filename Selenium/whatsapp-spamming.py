import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

targetProfile = input("Enter target profile: ")
msg = input("Enter the message to send: ")
spamTime = int(input("Enter spam time: "))

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://web.whatsapp.com/")
time.sleep(25)


driver.find_element(
    By.XPATH, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div").send_keys(targetProfile)
time.sleep(1)

allProfiles = driver.find_elements(
    By.CSS_SELECTOR, "#pane-side > div:nth-child(1) > div > div > div> div > div > div > div._8nE1Y > .y_sn4 > div._21S-L > div > span")
time.sleep(1)

for target in allProfiles:
    print(target.text)
    if targetProfile.lower() in target.text.lower():
        target.click()
        time.sleep(1)
        for i in range(0, spamTime):
            inputBox = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]")
            inputBox.send_keys(msg)
            inputBox.send_keys(Keys.ENTER)


time.sleep(3)
driver.close()

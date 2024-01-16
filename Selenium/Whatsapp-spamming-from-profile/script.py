import time

import config as cf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
profile = cf.local["userDataDir"]

options.add_argument(f"user-data-dir={profile}")

service = Service(cf.local["executablePath"])
targetProfile = input("Enter target profile: ")
msg = input("Enter the message to send: ")
spamTime = int(input("Enter spam time: "))

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com/")


def sendMessage(msg, to_whom, times) -> None:
    time.sleep(20)
    driver.find_element(
        By.XPATH, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div").send_keys(to_whom)

    time.sleep(1)

    allProfiles = driver.find_elements(
        By.CSS_SELECTOR, "#pane-side > div:nth-child(1) > div > div > div> div > div > div > div._8nE1Y > .y_sn4 > div._21S-L > div > span")
    time.sleep(1)

    for target in allProfiles:
        print(target.text)
        if to_whom.lower() in target.text.lower():
            target.click()
            time.sleep(1)
            for i in range(0, times):
                inputBox = driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]")
                inputBox.send_keys(msg)
                inputBox.send_keys(Keys.ENTER)

sendMessage(msg, targetProfile, spamTime)


driver.close()

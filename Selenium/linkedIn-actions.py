import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

print("Automation testing using selenium. ")
print("Tester's Name: Idris vohra")
print("Reviewer's Name: Raveena Ma'am")
print()

website = 'https://www.linkedin.com/authwall'
print(f"Navigating the website: {website}")
print()
driver.get(website)

# Data:
user_cred = {

}
post_data = {

}
edit_post_data = {

}
edit_user_data = {

}

# Functions:


def updateTitle(newTitle):
    driver.execute_script(f"document.title = '{newTitle}'")


def clickButton(id) -> None:
    print(f"Clicking button with id: {id}")
    print()

    driver.find_element(By.ID, id).click()


def fillForm(dataContext, request='insert') -> None:
    print(f"Filling up the form with {request} details..")
    print()

    print("Form values:")
    for i in range(0, len(dataContext)):
        key = list(dataContext.keys())[i]
        value = dataContext[key]
        print(f"{key} = {value}")

        elem = driver.find_element(By.ID, key)
        if request == "update":
            elem.clear()
        elem.send_keys(value)
    print()


updateTitle("Under testing by - Idris Vohra")


def CreateAccount():
    fillForm({"email-or-phone": "idris.vohra.sw@gmail.com",
             "password": "Idris987$"})
    clickButton("join-form-submit")
    time.sleep(1)
    fillForm({"first-name": "Idris",
             "last-name": "Vohra"})
    clickButton("join-form-submit")
    time.sleep(10)
    driver.find_element(By.NAME, "phoneNumber").send_keys("9106930717")
    # fillForm({"register-verification-phone-number": "9106930717"})

# <input type="text" name="phoneNumber" autocorrect="off" aria-required="true" validation="tel" id="register-verification-phone-number" validation-message="Oops, this isn't a valid phone number. Try entering it again." aria-describedby="register-phone-number-error" aria-label="please enter your phone number without county code">
CreateAccount()
time.sleep(15)

driver.close()

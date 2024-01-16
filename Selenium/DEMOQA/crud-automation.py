import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

print("Automation testing using selenium. ")
print("Tester's Name: Idris vohra")
print("Reviewer's Name: Raveena Ma'am")
print()

website = "https://demoqa.com/webtables"
print(f"Navigating the website: {website}")
print()

driver.get(website)



def TestingCRUD(driver):

    print("Testing CRUD Operations:")

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

    def updateTitle(newTitle):
        driver.execute_script(f"document.title = '{newTitle}'")

    insertData = {
        "firstName": "Idris",
        "lastName": "Vohra",
        "userEmail": "idris@gmail.com",
        "age": "20",
        "salary": "20000",
        "department": "Software Engineer",
    }

    insertData2 = {
        "firstName": "Jay",
        "lastName": "Dave",
        "userEmail": "jay@gmail.com",
        "age": "22",
        "salary": "20000",
        "department": "Software Engineer",
    }

    updateData = {
        "firstName": "Aryan",
        "lastName": "Sharma",
        "userEmail": "aryan@gmail.com",
        "age": "20",
        "salary": "20000",
        "department": "Software Engineer",
    }

    # Inserting 2 new entries:

    updateTitle("Inserting data")
    clickButton("addNewRecordButton")
    fillForm(insertData)
    clickButton("submit")

    clickButton("addNewRecordButton")
    fillForm(insertData2)
    clickButton("submit")

    # Deleting the entry 2 and 3:
    updateTitle("Deleting data")

    clickButton("delete-record-2")
    clickButton("delete-record-3")

    # Updating the entry 1:
    updateTitle("Updating data")
    clickButton("edit-record-1")
    fillForm(updateData, "update")
    clickButton("submit")

    print("All test successful!")
    print("Status: PASS")

TestingCRUD(driver)

time.sleep(5)
driver.close()
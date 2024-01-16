from selenium import webdriver
import unittest

class FormFillTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_fill_form(self):
        driver = self.driver
        driver.get("https://www.example.com/form")  # Replace with your form URL
        form_page = FormPage(driver)
        
        print("Starting form filling test...")

        # Fill up the form using Page Object Model
        print("Entering data into the form...")
        form_page.enter_name("John Doe")
        form_page.enter_email("johndoe@example.com")
        form_page.enter_message("This is a test message")
        form_page.click_submit_button()
        
        print("Form submitted successfully!")

        # Add assertions or verification steps if needed

    def tearDown(self):
        self.driver.close()

class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.name_field = "name"  # Replace with appropriate element locator
        self.email_field = "email"  # Replace with appropriate element locator
        self.message_field = "message"  # Replace with appropriate element locator
        self.submit_button = "submit"  # Replace with appropriate element locator

    def enter_name(self, name):
        print(f"Entering name: {name}")
        self.driver.find_element_by_id(self.name_field).send_keys(name)

    def enter_email(self, email):
        print(f"Entering email: {email}")
        self.driver.find_element_by_id(self.email_field).send_keys(email)

    def enter_message(self, message):
        print(f"Entering message: {message}")
        self.driver.find_element_by_id(self.message_field).send_keys(message)

    def click_submit_button(self):
        print("Clicking submit button...")
        self.driver.find_element_by_id(self.submit_button).click()

if __name__ == "__main__":
    unittest.main()

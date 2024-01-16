import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()


# Login
# Home page with sorting
# Shopping Cart
# Checkout

print("Automation testing using selenium. ")
print("Tester's Name: Idris vohra")
print("Reviewer's Name: Raveena Ma'am")
print()

website = 'https://www.saucedemo.com/'
print(f"Navigating the website: {website}")
print()

driver.get(website)

# Test Data:
right_login_data = {
    "user-name": "standard_user",
    "password": "secret_sauce"
}

wrong_login_data = {
    "user-name": "Idris",
    "password": "12345678"
}

products_to_cart_names = ["onesie", "bike-light", "fleece-jacket"]

checkout_info = {
  "first-name": "Idris",
  "last-name": "Vohra",
  "postal-code": "102020"
}

# Helper Functions:


def updateTitle(newTitle):
    driver.execute_script(f"document.title = '{newTitle}'")


def clickButton(value, by="id") -> None:
    print(f"Clicking button with {by}: {value}")
    print()

    driver.find_element(by, value).click()


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

# Test Scenarios:


# Validating Login functionality:

def Login(data):
    updateTitle("Testing Login functionality")

    print(f"Logging in using data : {data}")
    fillForm(data)
    clickButton("login-button")
    if driver.current_url == website:
        print("Login failed reason: Wrong data passed.")
        driver.refresh()
        return
    print("Login successful")
    print()


# Validating the sorting products functionality:

def Sorting(according=1):
    updateTitle("Testing sorting functionality")

    order = "Ascending"
    if according == 2:
        order = "Descending"
    elif according == 3:
        order = "Price (low to high)"
    elif according == 4:
        order = "Price (high to low)"

    print(f"Sorting products on {order} order")
    driver.find_element(
        By.CSS_SELECTOR, f"#header_container > div.header_secondary_container > div > span > select > option:nth-child({according})").click()
    print("Sorting successful..")
    print()

# Validating the add to cart products:


def AddProductsToCart(product_name):
    updateTitle("Testing add to cart products functionality")
    print(f"Adding product named: {product_name} to cart..")
    clickButton(f"add-to-cart-sauce-labs-{product_name}")
    print("Product added successfully...")
    print()

# Validating the remove from cart functionality:

def RemoveFromCart(product_name):
    updateTitle("Testing remove from cart products functionality")
    print(f"Removing product: {product_name} from the cart")
    clickButton(f"remove-sauce-labs-{product_name}")
    print("Product removed successfully..")
    print()

# Validating the checkout functionality:

def CheckOut():
    print("Testing checkout functionality")
    clickButton("#shopping_cart_container > a", "css selector")
    updateTitle("Testing checkout functionality")
    time.sleep(1)
    clickButton("checkout")
    time.sleep(1)
    fillForm(checkout_info)
    clickButton("continue")
    time.sleep(1)
    clickButton("finish")
    
# Test Cases:


# Wrong data passed in login form
Login(wrong_login_data)

# Right data passed in login form
Login(right_login_data)

# Sorting products based on the options provided:

Sorting()
time.sleep(4)
Sorting(2)
time.sleep(4)
Sorting(3)
time.sleep(4)
Sorting(4)

# Adding some products to the cart to test the cart functionality:

for product in products_to_cart_names:
    AddProductsToCart(product)

# Removing products from the cart to test the cart functionality:

RemoveFromCart("fleece-jacket")

# Validating the checkout functionality:

CheckOut()

print("All Tests Completed!")

print("All results have passed!")

time.sleep(15)

driver.close()

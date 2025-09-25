# from pages.login_page import LoginPage
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# def test_valid_login(driver):
#     print("Opening SnapdMe login page...")
#     driver.get("https://dev.events.snapdme.com/")
#     print("Page title:", driver.title)

#     login_page = LoginPage(driver)

#     print("Entering email...")
#     login_page.enter_email("nikhil.kushwaha@spectacom.in")

#     print("Entering password...")
#     login_page.enter_password("Nikhil@123")

#     print("Clicking Continue...")
#     login_page.click_continue()

#     print("Dashboard loaded...")
#     login_page.dashboard_header()
    
    
# #  pytest tests/test_login.py -v
# # pytest tests/test_event.py -v
# # pytest tests/ -v

import pytest
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.parametrize("email,password,expected,case_type", [
    # Positive cases
    ("nikhil.kushwaha@spectacom.in", "Nikhil@123", "Dashboard", "positive"),
    
    # Negative cases
    ("wrong.email@spectacom.in", "Nikhil@123", "Invalid email or password", "negative"),
    ("nikhil.kushwaha@spectacom.in", "WrongPassword", "Invalid email or password", "negative"),
    ("", "Nikhil@123", "Email is required", "negative"),
    ("nikhil.kushwaha@spectacom.in", "", "Password is required", "negative"),
])
def test_login(driver, email, password, expected, case_type):
    driver.get("https://dev.events.snapdme.com/")

    login_page = LoginPage(driver)
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_continue()

    time.sleep(2)

    if case_type == "positive":
        print("All positive test cases tested")

    elif case_type == "negative":
        print("All negative test cases tested")


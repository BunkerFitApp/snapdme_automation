from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    email_input = (By.XPATH, "//input[@placeholder='Email Address']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    continue_button = (By.XPATH, "//button[normalize-space()='Continue']")
    add_event_button = (By.XPATH, "//button[normalize-space()='Add New Event']")

    # Actions
    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()
 
    def dashboard_header(self):
        self.wait.until(EC.presence_of_element_located(self.add_event_button)).click()

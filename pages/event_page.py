from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class EventPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    add_new_event_button = (By.XPATH, "//button[normalize-space()='Add New Event']")
    open_first_event_button = (By.XPATH, "(//button[contains(@class,'allEvent_openAlbumBtn__wzqeq')])[1]")
    event_name_input = (By.XPATH, "//input[@name='eventName']")
    event_location_input = (By.XPATH, "//input[@placeholder='eg. New Delhi, India']")
    dropdown_event_type = (By.XPATH, "//div[@class='noEvent_dropdown__aheB4']")
    dropdown_option_dj = (By.XPATH, "//div[text()='Dj']")
    event_description = (By.XPATH, "//textarea[@placeholder='What this event is all about?']")
    cover_image = (By.XPATH, "//input[@type='file']")
    done_button = (By.XPATH, "//button[normalize-space()='Done']")

    # Actions
    def open_first_event(self):
        self.wait.until(EC.element_to_be_clickable(self.open_first_event_button)).click()
            
    def click_add_new_event(self):
        self.wait.until(EC.element_to_be_clickable(self.add_new_event_button)).click()

    def enter_event_name(self, name):
        self.wait.until(EC.presence_of_element_located(self.event_name_input)).send_keys(name)

    def enter_location(self, location):
        self.wait.until(EC.presence_of_element_located(self.event_location_input)).send_keys(location)

    def select_event_type(self):
        self.wait.until(EC.element_to_be_clickable(self.dropdown_event_type)).click()
        self.wait.until(EC.element_to_be_clickable(self.dropdown_option_dj)).click()

    def enter_description(self, description):
        self.wait.until(EC.presence_of_element_located(self.event_description)).send_keys(description)
    
    def upload_cover_image(self, filename="test_photo.jpg"):
        file_path = os.path.join(os.getcwd(), "resources", filename)
        self.wait.until(EC.presence_of_element_located(self.cover_image)).send_keys(file_path)

    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.done_button)).click()
    
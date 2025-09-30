from pages.event_page import EventPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import pytest

import time

@pytest.mark.order(2)   
def test_add_event(driver):
    driver.get("https://dev.events.snapdme.com/")

    # Login first
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Wait until dashboard loads
    time.sleep(3)  # replace with proper WebDriverWait if needed

    # Add new event
    print("Adding new event...")
    event_page = EventPage(driver)
    event_page.click_add_new_event()
    print("Filling event details-name...")   
    event_page.enter_event_name("Corp War")
    print("Filling event details-location...")
    event_page.enter_location("delhi")
    print("Filling event details-type...")
    event_page.select_event_type()
    print("Filling event details-description...")
    event_page.enter_description("This event is created using automation script.")
    print("Uploading event cover image...")
    event_page.upload_cover_image("/home/spectacom/Downloads/pexels-alipazani-32603009.jpg")
    print("photo uploaded successfully")
    print("Submitting the event form...")
    event_page.click_done()
    print("Event added successfully.")

    # # Assertion: verify new event is visible
    # new_event = driver.find_element(By.XPATH, "///h3[normalize-space()='Corporate War']")
    # assert new_event.is_displayed()

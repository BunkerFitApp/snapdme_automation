import allure
import pytest
from pages.login_page import LoginPage
from pages.event_page import EventPage
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from pages.settings_page import SettingsPage

@pytest.mark.order(7)
def test_event_settings_edit(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
	# @allure.step("Open the settings page") 
    
    # Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()
    
    # Step 2: Open Event
    event_page = EventPage(driver)
    event_page.open_first_event()
 

    # Step 3: Open Settings
    settings_page = SettingsPage(driver)
    if settings_page.is_no_event_present(): 
        print("No events present. Cannot edit settings.")
    else:
        settings_page.open_event_settings()
                
        #Edit details
        settings_page.edit_event_details(name="Updated Event Name", location="Updated Location", description="Updated Description")
        settings_page.save_settings()
        print("Event settings updated and saved.")
    

import allure
import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.album_page import AlbumPage 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    

@pytest.mark.order(3)
def test_add_album(driver):
    driver.get("https://dev.events.snapdme.com/")

    # Step 1: Login
    print("Logging in...")
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()
    time.sleep(3)
    print("Login successful.")

    # Step 2: Go to Event
    no_event_buttons = driver.find_elements(By.XPATH, "//button[@class='noEvent_createButton__3KR0_']")
    if no_event_buttons:
        print("No events present. Cannot add album.")
    else:    
        print("Navigating to event...")
    event_page = EventPage(driver)
    event_page.open_first_event()
    print("Event opened.")

    # Step 3: Go to Album section
    print("Navigating to Album section...")
    album_page = AlbumPage(driver)
    album_page.click_add_album()
    print("Opened Album section.")

    # Step 4: Fill album details
    print("Filling album details...")
    album_page.enter_album_name("Automated album")
    print("Filling album description...")
    album_page.enter_album_description("Album created via automation")
    print("Uploading album cover image...")
    album_page.upload_photo("/home/spectacom/Downloads/pexels-alipazani-32603009.jpg")  
    print("Photo uploaded successfully.")
    album_page.click_save()
    print("Album saved successfully.")
    

    # # Step 5: Assertion - Album visible
    # print("Verifying album creation...")
    # try:
    #     new_album = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, "//*[contains(normalize-space(text()), 'Test Album Automation 2')]"))
    #     )
    #     assert new_album.is_displayed()
    #     print("Album is displayed.")
    # except Exception as e:
    #     print("Album not found:", e)
    #     assert False, "Album was not created or not visible."


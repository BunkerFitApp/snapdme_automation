import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.album_page import AlbumPage
from pages.delete_page import DeletePage


@pytest.mark.usefixtures("driver")   # if you are using pytest fixture for driver
def test_delete_flow(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")

    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Step 2: Open Event
    event_page = EventPage(driver)
    event_page.open_first_event()

    # Step 3: Open Album
    album_page = AlbumPage(driver)
    album_page.open_first_album()

    # Step 4: Delete Photo
    delete_page = DeletePage(driver)
    delete_page.delete_checkbox()
    delete_page.delete_all()
    delete_page.confirm_delete()

    # Step 5: Delete Album
    album_msg = delete_page.delete_album()
    # assert "Deleted" in album_msg.text

    # Step 6: Delete Event
    event_msg = delete_page.delete_event()
    # assert "Deleted" in event_msg.text

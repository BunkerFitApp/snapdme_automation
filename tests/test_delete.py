import allure
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.album_page import AlbumPage
from pages.delete_page import DeletePage


@pytest.mark.usefixtures("driver") 
@pytest.mark.order(5)
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
    no_event_buttons = driver.find_elements(By.XPATH, "//button[@class='noEvent_createButton__3KR0_']")
    if no_event_buttons:
        print("No events present. Cannot share event.")
    else:
        event_page.open_first_event()

        # Step 3: Open Album
        album_page = AlbumPage(driver)
        first_album_card = (By.XPATH,"//div[contains(@class,'allAlbum_albumCard__')][1]//button[normalize-space()='Upload Photos']")
        if first_album_card:
            album_page.open_first_album()

        # Step 4: Delete Photo
            delete_page = DeletePage(driver)
            delete_buttons = driver.find_elements(By.XPATH, "//button[@class='NoPhoto_chooseFilesButton__hzQAi']")
            if not delete_buttons:
                print("No photos present. Cannot delete photos.")
            else:
                delete_page.delete_checkbox()
                delete_page.delete_all()
                delete_page.confirm_delete()
        else:
            print("No albums present. Cannot delete album.")        

    # Step 5: Delete Album
    # album_msg = delete_page.delete_album()
    # assert "Deleted" in album_msg.text

    # Step 6: Delete Event
    # event_msg = delete_page.delete_event()
    # assert "Deleted" in event_msg.text

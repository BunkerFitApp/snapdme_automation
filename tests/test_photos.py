import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.album_page import AlbumPage 
from pages.photos_page import PhotosPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    


def test_upload_photo(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    print("a")
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Step 2: Open first event
    event_page = EventPage(driver)
    event_page.open_first_event()

    # Step 3: Open first album and go to photos
    album_page = AlbumPage(driver)
    print("g")
    album_page.open_first_album()
    print("h")
    # album_page.click_upload_photos_on_card()
 
    # Step 4: Upload photo
    photos_page = PhotosPage(driver)
    print("i")  
    # photos_page.click_upload_photo_top()
    # print("j")
    photos_page.upload__photo("/home/spectacom/Downloads/pexels-nkhajotia-1516680.jpg")
    print("k")      
    photos_page.click_upload_all_image()
    print("l")  
    photos_page.click_save()
    print("m")

    # Assertion (example: success toast or photo thumbnail visible)
    success_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Upload Successful')]")
    assert success_msg.is_displayed()

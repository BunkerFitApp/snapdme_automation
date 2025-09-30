import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.album_page import AlbumPage 
from pages.photos_page import PhotosPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    

@pytest.mark.order(4)
def test_upload_photo(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    print("starting test case")
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
    print("album page")
    driver.save_screenshot("/home/spectacom/picc/a.png")
    
    create_album_btn = (By.XPATH, "//img[@alt='Create']")

    album_page.open_first_album()
    driver.save_screenshot("/home/spectacom/picc/b.png")

 
    # Step 4: Upload photo
    photos_page = PhotosPage(driver)
    driver.save_screenshot("/home/spectacom/picc/c.png")
    upload__photos_button = (By.XPATH, "//button[@class='UploadPhoto_uploadButton___2gLe']")  
    if upload__photos_button:
        print("Upload photo button found, proceeding to upload.")

     
    
    # photos_page.upload__photos("/home/spectacom/Downloads/pexels-latronico-709188.jpg")
    # print("k")      
    # driver.save_screenshot("/home/spectacom/picc/d.png")
    
    # photos_page.click_upload_all_image()
    # print("l")  
    # driver.save_screenshot("/home/spectacom/picc/e.png")



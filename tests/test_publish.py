import allure
import time
import pytest
from pages.login_page import LoginPage
from pages.publish_page import PublishPage
from pages.event_page import EventPage

from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC    

@pytest.mark.order(6)
def test_publish_event_1(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    publish_page = PublishPage(driver)
    no_event_buttons = driver.find_elements(By.XPATH, "//button[@class='noEvent_createButton__3KR0_']")
    if no_event_buttons:
        print("No events present. Cannot add album.")
    else:      
        publish_page.click_publish_event_1()
        print("Event UnPublished successfully")
        driver.save_screenshot("/home/spectacom/picc/20.png")
    # publish_page.click_publish_event_1()
    # print("Event Published successfully")
    # driver.save_screenshot("/home/spectacom/picc/21.png")
    
@pytest.mark.order(6)
def test_publish_event_2(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    #step 2: open first event
    event_page = EventPage(driver)
    no_event_buttons = driver.find_elements(By.XPATH, "//button[@class='noEvent_createButton__3KR0_']")
    if no_event_buttons:
        print("No events present. Cannot share event.")
    else:
        event_page.open_first_event()
        publish_page = PublishPage(driver)

        publish_page.click_publish_event_2()
        print("Event UnPublished successfully")
        driver.save_screenshot("/home/spectacom/picc/22.png")
    # publish_page.click_publish_event_2()
    # print("Event Published successfully")
    # driver.save_screenshot("/home/spectacom/picc/23.png")
    

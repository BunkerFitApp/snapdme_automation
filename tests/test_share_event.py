import allure
import pytest
from selenium import webdriver
from pages.event_page import EventPage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.event_page import EventPage
from pages.share_event_page import ShareEventPage   

@pytest.mark.order(8)
def test_share_method_1(driver):
    
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()    
    
    #share metod 1
    share_event_page = ShareEventPage(driver)
    driver.save_screenshot("/home/spectacom/picc/11.png")
    share_event_page.click_share_1()   
    driver.save_screenshot("/home/spectacom/picc/12.png")
    share_event_page.copy_icon()
    driver.save_screenshot("/home/spectacom/picc/13.png")
    print("sharing event method 1 passed")    
 
@pytest.mark.order(8)
def test_share_method_2(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()    
    print("sharing event method 2 passed")    
    
        
    share_event_page = ShareEventPage(driver)
    driver.save_screenshot("/home/spectacom/picc/14.png")   
    share_event_page.click_share_2()

@pytest.mark.order(8)
def test_share_method_3(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()      
    print("sharing event method 3 passed")  
    
    #step 2: open first event
    event_page = EventPage(driver)
    event_page.open_first_event()
    
            
    share_event_page = ShareEventPage(driver)
    create_album_btn = (By.XPATH, "//img[@alt='Create']")
   
    share_event_page.click_share_3()
    share_event_page.copy_icon()
    driver.save_screenshot("/home/spectacom/picc/17.png")




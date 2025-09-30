from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShareEventPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    share_button_1 = (By.XPATH, "//div[@class='allEvent_mainContent__hQDro']//div[1]//div[1]//div[1]//button[1]")
    share_button_2 = (By.XPATH, "//div[@class='allEvent_mainContent__hQDro']//div[1]//div[2]//div[2]//button[2]")
    share_button_3 = (By.XPATH, "//div[@class='allAlbum_headerRight__jP1I8']//button[1]")

    # Actions
    def click_share_1(self):
        self.wait.until(EC.element_to_be_clickable(self.share_button_1)).click()
    
    def click_share_2(self):
        self.wait.until(EC.element_to_be_clickable(self.share_button_2)).click()
        
    def click_share_3(self):
        self.wait.until(EC.element_to_be_clickable(self.share_button_3)).click()    
            
    def copy_icon(self):
        copy_icon_locator = (By.XPATH, "//div[@class='shareModal_shareOptions__apOXP']//button[1]")
        self.wait.until(EC.element_to_be_clickable(copy_icon_locator)).click()
    
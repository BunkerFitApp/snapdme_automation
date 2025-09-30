
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PhotosPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    file_input = (By.XPATH, "//input[@type='file']")
    
    upload__photos_button = (By.XPATH, "//button[@class='UploadPhoto_uploadButton___2gLe']")  
    upload_all_image_button = (By.XPATH, "//div[contains(@class,'ImagePreviewModal_footerRight')]//button[2]")

    # Actions
       
    def upload__photos(self, file_path):
        input_element = self.wait.until(EC.presence_of_element_located(self.file_input))
        input_element.send_keys(file_path)
        
    def click_upload_all_image(self):
        self.wait.until(EC.element_to_be_clickable(self.upload_all_image_button)).click()


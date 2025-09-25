from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PhotosPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    # upload_photo_top_button = (By.XPATH, "//button[contains(text(),'Upload Photo')]")
    upload_all_image_button = (By.XPATH, "//div[contains(@class,'ImagePreviewModal_footerRight')]//button[2]")
    upload_button = (By.XPATH, "//button[starts-with(text(), 'Upload')]")
    photo_input= (By.CSS_SELECTOR, "input[type='file']")


    save_button = (By.XPATH, "//button[normalize-space()='Done']")

    # Actions
    # def click_upload_photo_top(self):
    #     self.wait.until(EC.element_to_be_clickable(self.upload_photo_top_button)).click()

    def upload__photo(self, file_path):
        # self.wait.until(EC.presence_of_element_located(self.photo_input)).click()
        self.wait.until(EC.presence_of_element_located(self.photo_input)).send_keys(file_path)
        
    def click_upload_all_image(self):
        self.wait.until(EC.element_to_be_clickable(self.upload_all_image_button)).click()



    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
        

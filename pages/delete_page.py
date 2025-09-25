from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    delete_checkbox_button = (By.XPATH, "//div[contains(@class,'UploadPhoto_gridImage')]//input[@type='checkbox'])[1]")
    delete_all_button = (By.XPATH, "//img[@alt='Delete']")
    confirm_delete_button = (By.XPATH, " //img[@alt='Delete']")
    # cancel_delete_button = (By.XPATH, "//button[normalize-space()='No']")


    # Actions
    def delete_checkbox(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_checkbox_button)).click()
        
    def delete_all(self):    
        self.wait.until(EC.element_to_be_clickable(self.delete_all_button)).click()

    def confirm_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button)).click()
        


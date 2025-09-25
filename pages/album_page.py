from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 



class AlbumPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators
    open_album_button = (By.XPATH, "//div[@class='allEvent_mainContent__hQDro']//div[1]//div[2]//div[2]//button[1]")
    create_album_btn = (By.XPATH, "//img[@alt='Create']")
    add_album_btn = (By.XPATH, "//img[@alt='Upload']")
    album_name_input = (By.XPATH, "//input[@placeholder='Wedding Photography']")
    album_description_input = (By.XPATH, "//textarea[@placeholder='What this album is all about?']")
    photo_upload_input = (By.XPATH, "//input[@type='file']")
    save_button = (By.XPATH, "//button[normalize-space()='Done']")
    first_album_card = (By.XPATH,"//div[contains(@class,'allAlbum_albumCard__')][1]")
    # upload_photos_button = (By.XPATH, "(//button[contains(text(),'Upload Photos'])[1]")


    # Actions
    
    def click_open_album(self):
        self.driver.find_element(*self.open_album_button).click()
        
    def open_first_album(self):
        self.wait.until(EC.element_to_be_clickable(self.first_album_card)).click()
        
    # def click_upload_photos_on_card(self):
    #     self.wait.until(EC.element_to_be_clickable(self.upload_photos_button)).click()

    
    def click_add_album(self):
        try:
            # Case 1: "Create Album" button in center (when no albums exist)
            create_album_btn = self.wait.until(
                EC.element_to_be_clickable(self.create_album_btn)
            )
            print("No albums exist, clicking 'Create Album'")
            create_album_btn.click()
        except TimeoutException:
            # Case 2: "Add Album" button on top (when albums already exist)
            add_album_btn = self.wait.until(
                EC.element_to_be_clickable(self.add_album_btn)
            )
            print("Albums exist, clicking 'Add Album'")
            add_album_btn.click()
    
    def enter_album_name(self, name):
        self.driver.find_element(*self.album_name_input).send_keys(name)

    def enter_album_description(self, description):
        self.driver.find_element(*self.album_description_input).send_keys(description)

    def upload_photo(self, file_path):
        self.driver.find_element(*self.photo_upload_input).send_keys(file_path)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()
 
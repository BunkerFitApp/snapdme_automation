from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PublishPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	# Locators
	publish_1_button = (By.XPATH, "//body[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]")
	publish_2_button = (By.XPATH, "//div[@class='allAlbum_headerRight__jP1I8']//div[contains(@class,'allAlbum_toggleOn__')] | //div[@class='allAlbum_headerRight__jP1I8']//div[contains(@class,'allAlbum_toggleOff__')]")

	# Actions
	def click_publish_event_1(self):
		self.wait.until(EC.element_to_be_clickable(self.publish_1_button)).click()

	def click_publish_event_2(self):
		self.wait.until(EC.element_to_be_clickable(self.publish_2_button)).click()

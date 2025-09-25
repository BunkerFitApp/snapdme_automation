from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PublishPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	# Locators
	sidebar_publish_button = (By.XPATH, "//span[contains(text(),'Publish')]/parent::button")
	publish_event_button = (By.XPATH, "//button[contains(text(),'Publish Event')]")
	confirm_publish_button = (By.XPATH, "//button[contains(text(),'Confirm')]")
	success_message = (By.XPATH, "//*[contains(text(),'Event published successfully')]")

	# Actions
	def click_publish_sidebar(self):
		self.wait.until(EC.element_to_be_clickable(self.sidebar_publish_button)).click()

	def click_publish_event(self):
		self.wait.until(EC.element_to_be_clickable(self.publish_event_button)).click()

	def confirm_publish(self):
		self.wait.until(EC.element_to_be_clickable(self.confirm_publish_button)).click()

	def get_success_message(self):
		return self.wait.until(EC.presence_of_element_located(self.success_message)).text

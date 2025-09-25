from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShareEventPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	# Locators
	sidebar_share_event_button = (By.XPATH, "//span[contains(text(),'Share Event')]/parent::button")
	copy_link_button = (By.XPATH, "//button[contains(text(),'Copy Link')]")
	event_link_input = (By.XPATH, "//input[@readonly and contains(@value,'snapdme.com')]")

	# Actions
	def click_share_event_sidebar(self):
		self.wait.until(EC.element_to_be_clickable(self.sidebar_share_event_button)).click()

	def copy_event_link(self):
		self.wait.until(EC.element_to_be_clickable(self.copy_link_button)).click()
		link = self.wait.until(EC.presence_of_element_located(self.event_link_input)).get_attribute('value')
		return link

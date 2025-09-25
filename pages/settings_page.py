from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SettingsPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	# Locators
	event_settings_button = (By.XPATH, "//button[contains(@class,'event_settings_btn')]")
	event_name_input = (By.XPATH, "//input[@placeholder='Event Name']")
	event_location_input = (By.XPATH, "//input[@placeholder='eg. New Delhi, India']")
	event_description_input = (By.XPATH, "//textarea[@placeholder='What this event is all about?']")
	done_button = (By.XPATH, "//button[normalize-space()='Done']")
	no_event_text = (By.XPATH, "//*[contains(text(),'No events found')]")

	# Actions
	def open_event_settings(self):
		try:
			self.wait.until(EC.element_to_be_clickable(self.event_settings_button)).click()
			return True
		except TimeoutException:
			# No event present
			return False

	def edit_event_details(self, name=None, location=None, description=None):
		if name:
			name_input = self.wait.until(EC.presence_of_element_located(self.event_name_input))
			name_input.clear()
			name_input.send_keys(name)
		if location:
			location_input = self.wait.until(EC.presence_of_element_located(self.event_location_input))
			location_input.clear()
			location_input.send_keys(location)
		if description:
			desc_input = self.wait.until(EC.presence_of_element_located(self.event_description_input))
			desc_input.clear()
			desc_input.send_keys(description)

	def save_settings(self):
		self.wait.until(EC.element_to_be_clickable(self.done_button)).click()

	def is_no_event_present(self):
		try:
			self.wait.until(EC.presence_of_element_located(self.no_event_text))
			return True
		except TimeoutException:
			return False

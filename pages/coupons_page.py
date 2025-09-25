from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CouponsPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	# Locators
	sidebar_coupon_button = (By.XPATH, "//span[contains(text(),'Coupons')]/parent::button")
	tile_locators = [
		(By.XPATH, "(//div[contains(@class,'coupon_tile__')])[1]//span"),
		(By.XPATH, "(//div[contains(@class,'coupon_tile__')])[2]//span"),
		(By.XPATH, "(//div[contains(@class,'coupon_tile__')])[3]//span"),
		(By.XPATH, "(//div[contains(@class,'coupon_tile__')])[4]//span")
	]
	coupon_row_locator = (By.XPATH, "//div[contains(@class,'coupon_row__')]")
	coupon_name_locator = (By.XPATH, ".//div[contains(@class,'coupon_name__')]")
	coupon_detail_locator = (By.XPATH, ".//div[contains(@class,'coupon_detail__')]")

	# Actions
	def click_coupon_sidebar(self):
		self.wait.until(EC.element_to_be_clickable(self.sidebar_coupon_button)).click()

	def get_tile_values(self):
		values = []
		for locator in self.tile_locators:
			value = self.wait.until(EC.presence_of_element_located(locator)).text
			values.append(value)
		return values

	def get_coupon_list(self):
		coupons = []
		rows = self.driver.find_elements(*self.coupon_row_locator)
		for row in rows:
			name = row.find_element(*self.coupon_name_locator).text
			detail = row.find_element(*self.coupon_detail_locator).text
			coupons.append({'name': name, 'detail': detail})
		return coupons

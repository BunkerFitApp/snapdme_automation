from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CouponsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

	# Locators
    sidebar_coupon_button = (By.XPATH, "//div[contains(@class,'sidebar_navigation__vbx0_')]//div[2]")
    tile_locators = [
        (By.XPATH, "//body/div[@id='__next']/div/main/div/section[@class='couponsStats_couponsStatsContainer__o58AJ']/div[@class='couponsStats_couponsStats__OsFWH']/div[@class='couponsStats_statsCardsContainer__Fu4ht']/div[1]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/section[@class='couponsStats_couponsStatsContainer__o58AJ']/div[@class='couponsStats_couponsStats__OsFWH']/div[@class='couponsStats_statsCardsContainer__Fu4ht']/div[2]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/section[@class='couponsStats_couponsStatsContainer__o58AJ']/div[@class='couponsStats_couponsStats__OsFWH']/div[@class='couponsStats_statsCardsContainer__Fu4ht']/div[3]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/section[@class='couponsStats_couponsStatsContainer__o58AJ']/div[@class='couponsStats_couponsStats__OsFWH']/div[@class='couponsStats_statsCardsContainer__Fu4ht']/div[4]"),
	]
 
    # Locator for coupon rows
    coupon_row_locator = (By.XPATH, "//div[contains(@class,'rdt_TableBody')]/div[contains(@class,'rdt_TableRow')]")
 
 
	# Actions
    def click_coupon_sidebar(self):
        self.wait.until(EC.element_to_be_clickable(self.sidebar_coupon_button)).click()

    def get_tile_values(self):
        values = []
        for locator in self.tile_locators:
            value = self.wait.until(
                lambda driver: "Loading..." not in driver.find_element(*locator).text
            )
            value =self.driver.find_element(*locator).text.strip()
            values.append(value)
        return values


    def get_coupon_list(self):
        coupons = []

        rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.coupon_row_locator)
        )

        for row in rows:
            event_name = row.find_element(By.XPATH, ".//div[@data-column-id='1']//span").text
            coupon_issued = row.find_element(By.XPATH, ".//div[@data-column-id='2']").text
            event_status = row.find_element(By.XPATH, ".//div[@data-column-id='3']//span").text
            total_redemption = row.find_element(By.XPATH, ".//div[@data-column-id='4']//span[1]").text.strip()
            upload_date = row.find_element(By.XPATH, ".//div[@data-column-id='5']").text

            coupons.append({
                "event_name": event_name,
                "coupon_issued": coupon_issued,
                "event_status": event_status,
                "total_redemption": total_redemption,
                "upload_date": upload_date
            })

        print(f"✅ Found {len(coupons)} coupons")
        return coupons


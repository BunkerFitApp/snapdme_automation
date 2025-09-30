from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ------------------ Locators ------------------
    sidebar_settings_button = (By.XPATH, "//div[contains(@class,'sidebar_navigation__vbx0_')]//div[4]")
    subscriptions_menu_item = (By.XPATH, "//div[contains(@class,'sidebar_settingsDropdown__RGVXZ')]//div[5]")

    # Plan info locators
    current_plan_locator = (By.XPATH, "//div[contains(@class,'subscription-billing_planName__8C_6B')]")
    plan_price_locator = (By.XPATH, "//div[contains(@class,'subscription-billing_planPrice__PDNkk')]")
    billing_cycle_locator = (By.XPATH, "//div[contains(@class,'subscription-billing_planDetailRow__lv8Jc')][1]")
    renewal_date_locator = (By.XPATH, "//div[contains(@class,'subscription-billing_planDetailRow__lv8Jc')][2]")
    payment_method_locator = (By.XPATH, "//div[contains(@class,'subscription-billing_planDetailRow__lv8Jc')][3]")




    # Billing history table
    billing_rows_locator = (By.XPATH, "//table[contains(@class,'billingTable')]//tbody/tr")
    billing_date_locator = (By.XPATH, "./td[1]")
    billing_amount_locator = (By.XPATH, "./td[2]")
    billing_status_locator = (By.XPATH, "./td[3]/span")

    # ------------------ Actions ------------------
    def open_subscriptions_page(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.sidebar_settings_button)).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.subscriptions_menu_item)).click()

    def get_plan_info(self):
        plan_info = {
            "current_plan": self.wait.until(EC.presence_of_element_located(self.current_plan_locator)).text,
            "plan price": self.wait.until(EC.presence_of_element_located(self.plan_price_locator)).text,
            "billing_cycle": self.wait.until(EC.presence_of_element_located(self.billing_cycle_locator)).text,
            "renewal_date": self.wait.until(EC.presence_of_element_located(self.renewal_date_locator)).text,
            "payment_method": self.wait.until(EC.presence_of_element_located(self.payment_method_locator)).text,
        }
        return plan_info

    def get_billing_history(self):
        history = []
        rows = self.driver.find_elements(*self.billing_rows_locator)
        for row in rows:
            history.append({
                "date": row.find_element(*self.billing_date_locator).text,               
                "amount": row.find_element(*self.billing_amount_locator).text,
                "status": row.find_element(*self.billing_status_locator).text
            })
        return history

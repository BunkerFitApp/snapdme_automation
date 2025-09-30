from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class RevenuePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Locators
    sidebar_revenue_button = (By.XPATH, "//div[contains(@class,'sidebar_navigation__vbx0_')]//div[3]")
    tile_locators = [
        (By.XPATH, "//body/div[@id='__next']/div/main/div/div[@class='revenueStats_revenueStatsContainer__XOeiD']/div[@class='revenueStats_revenueStats__rN6c0']/div[@class='revenueStats_revenueStatsContent__DlSbZ']/div[@class='revenueStats_statsBoxes__06O3j']/div[1]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/div[@class='revenueStats_revenueStatsContainer__XOeiD']/div[@class='revenueStats_revenueStats__rN6c0']/div[@class='revenueStats_revenueStatsContent__DlSbZ']/div[@class='revenueStats_statsBoxes__06O3j']/div[2]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/div[@class='revenueStats_revenueStatsContainer__XOeiD']/div[@class='revenueStats_revenueStats__rN6c0']/div[@class='revenueStats_revenueStatsContent__DlSbZ']/div[@class='revenueStats_statsBoxes__06O3j']/div[3]"),
        (By.XPATH, "//body/div[@id='__next']/div/main/div/div[@class='revenueStats_revenueStatsContainer__XOeiD']/div[@class='revenueStats_revenueStats__rN6c0']/div[@class='revenueStats_revenueStatsContent__DlSbZ']/div[@class='revenueStats_statsBoxes__06O3j']/div[4]"),
    ]
    revenue_row_locator = (By.XPATH, "//div[@class='sc-eqNDNG lnqPEg rdt_TableBody']/div[contains(@class,'sc-dYwGCk bgnHIy rdt_TableRow')]")

    # Actions
    def click_revenue_sidebar(self):
        self.wait.until(EC.element_to_be_clickable(self.sidebar_revenue_button)).click()

    def get_tile_values(self):
        values = []
        for locator in self.tile_locators:
            element = WebDriverWait(self.driver,15).until(
                lambda d:re.search(r'\d+',d.find_element(*locator).text) and d.find_element(*locator))
            values.append(element.text)
        return values

    def get_revenue_list(self):
        revenue_list = []
        # Wait until at least one revenue row is present
        rows = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(self.revenue_row_locator))
        
        for row in rows:
            payment_id = self.wait.until(EC.presence_of_element_located((By.XPATH, ".//div[@data-column-id='1']"))).text
            user_email = row.find_element(By.XPATH, ".//div[@data-column-id='2']//div[contains(@class,'revenueDetails_userEmail')]").text
            amount_paid = row.find_element(By.XPATH, ".//div[@data-column-id='3']//span").text
            platform_fee = row.find_element(By.XPATH, ".//div[@data-column-id='4']//span").text
            processing_fee = row.find_element(By.XPATH, ".//div[@data-column-id='5']//span").text
            payment_status = row.find_element(By.XPATH, ".//div[@data-column-id='6']//span").text

            revenue_list.append({
                "payment_id": payment_id,
                "user_email": user_email,
                "amount_paid": amount_paid,
                "platform_fee": platform_fee,
                "processing_fee": processing_fee,
                "payment_status": payment_status
            })
        return revenue_list

    def calculate_total_revenue(self):
        revenues = self.get_revenue_list()
        total = 0.0
        for rev in revenues:
            try:
                amt = float(rev['amount_paid'].replace(',', '').replace('₹', '').strip())
                total += amt
            except Exception:
                pass
        return total

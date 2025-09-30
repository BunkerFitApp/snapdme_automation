import allure
import pytest
from selenium import webdriver
import re
import math
from pages.login_page import LoginPage
from pages.revenue_page import RevenuePage

@pytest.mark.order(10)
def test_revenue_flow(driver):
    @allure.step("Open the revenue page")
    def open_revenue_page(driver):
        driver.get("https://dev.events.snapdme.com/")

    @allure.step("Get all tile values")
    def get_tile_values(driver):
        tiles = driver.find_elements_by_class_name("tile-class")
        for tile in tiles:
            allure.attach(tile.text, name="Tile Value", attachment_type=allure.attachment_type.TEXT)

    # Step 1: Open revenue page
    open_revenue_page(driver)

    # Step 2: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Step 3: Go to Revenue page via sidebar
    revenue_page = RevenuePage(driver)
    revenue_page.click_revenue_sidebar()

    # Step 4: Print tile values
    tile_values = revenue_page.get_tile_values()
    print(f"Number of tiles found: {len(tile_values)}")
    print("Revenue Tile Values:")
    for idx, value in enumerate(tile_values, 1):
        print(f"Tile {idx}: {value}")

    # Step 5: Verify first tile = sum of third + fourth
    tile_numbers = []
    for value in tile_values[:]:
        match = re.search(r'(\d+)', value.replace(',', ''))
        if match:
            tile_numbers.append(int(match.group(1)))
        else:
            tile_numbers.append(0)  

    if tile_numbers[0] == tile_numbers[2] + tile_numbers[3]:
        print(f"✅ Sum Match: Total Payments={tile_numbers[0]} is equal to sum of Successful Payments={tile_numbers[2]} and Failed Payments={tile_numbers[3]}")
    else:
        print(f"❌ Sum Mismatch: Total Payments={tile_numbers[0]} is not equal to sum of Successful Payments={tile_numbers[2]} and Failed Payments={tile_numbers[3]}")

    # Step 6: Print revenue list
    revenue_list = revenue_page.get_revenue_list()
    print("Revenue List:")
    for rev in revenue_list:
        print(f"Payment ID: {rev['payment_id']}, User: {rev['user_email']}, Amount: {rev['amount_paid']}, Platform Fee: {rev['platform_fee']}, Processing Fee: {rev['processing_fee']}, Status: {rev['payment_status']}")

    # Step 7: Print total revenue
    total = revenue_page.calculate_total_revenue()
    total_rounded = round(total)
    print(f"Total Revenue: ₹{total}")
    print(f"Total Rounded Revenue: ₹{total_rounded}")
    print(f"Displayed Total Amount Paid from Tile: ₹{tile_numbers[1]}")
    if tile_numbers[1] == total_rounded:
        print(f"✅ Total Revenue Match: Displayed Total Amount Paid ₹{tile_numbers[1]} matches Calculated Total Revenue ₹{total_rounded}")
    else:
        print(f"❌ Total Revenue Mismatch: Displayed Total Amount Paid ₹{tile_numbers[1]} does not match Calculated Total Revenue₹{total_rounded}")
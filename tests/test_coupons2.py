import allure
import math
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.coupons_page import CouponsPage


@pytest.mark.order(9)
def test_coupons_flow(driver):
    driver.maximize_window()
    driver.get("https://dev.events.snapdme.com/")
    

    # Step 2: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Step 3: Go to Coupons page via sidebar
    coupons_page = CouponsPage(driver)
    coupons_page.click_coupon_sidebar()

    # Step 4: Print tile values
    tile_values = coupons_page.get_tile_values()
    print(f"Number of tiles found: {len(tile_values)}")
    tile_numbers = [int(value.split("\n")[-1]) for value in tile_values[:3]]
    print("Tile Values:")
    for idx, value in enumerate(tile_values, 1):
        print(f"Tile {idx}: {value}")
  
    # Step 5: Verify first tile = sum of second + third
    if tile_numbers[0] == tile_numbers[1] + tile_numbers[2]:
        print(f"✅ Sum Match: Total={tile_numbers[0]} is equal to sum of Redeemed={tile_numbers[1]} and Pending={tile_numbers[2]}")
    else:
        print(f"❌ Sum Mismatch: Total={tile_numbers[0]} is not equal to sum of Redeemed={tile_numbers[1]} and Pending={tile_numbers[2]}")
    
    # Step 6: Verify fourth tile = (first/second)*100   
    # Calculate expected percentage using floor
    expected_rate = math.floor((tile_numbers[1] / tile_numbers[0]) * 100) if tile_numbers[0] != 0 else 0

    # Extract actual redemption rate
    redemption_rate_str = tile_values[3].split("\n")[-1]  # e.g., '2%'
    redemption_rate = int(redemption_rate_str.replace('%', ''))
  
    if redemption_rate == expected_rate:
        print(f"✅ Percentage Rate Match: {redemption_rate}% is correct")
    else:
        print(f"❌ Percentage Rate Mismatch: {redemption_rate}% is incorrect")  
        
                 
    coupon_list = coupons_page.get_coupon_list()    
    print("Coupon List:")
    for coupon in coupon_list:
        print(f"Event Name: {coupon['event_name']}, Coupons Issued: {coupon['coupon_issued']}, "
        f"Status: {coupon['event_status']}, Total Redemption: {coupon['total_redemption']}, "
        f"Upload Date: {coupon['upload_date']}")
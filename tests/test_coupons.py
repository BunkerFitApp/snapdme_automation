import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.coupons_page import CouponsPage

def test_coupons_flow(driver):
	driver.get("https://dev.events.snapdme.com/")

	# Login
	login_page = LoginPage(driver)
	login_page.enter_email("your_email@example.com")
	login_page.enter_password("your_password")
	login_page.click_continue()

	# Go to Coupons page via sidebar
	coupons_page = CouponsPage(driver)
	coupons_page.click_coupon_sidebar()

	# Print tile values
	tile_values = coupons_page.get_tile_values()
	print("Tile Values:")
	for idx, value in enumerate(tile_values, 1):
		print(f"Tile {idx}: {value}")

	# Print coupon list
	coupon_list = coupons_page.get_coupon_list()
	print("Coupon List:")
	for coupon in coupon_list:
		print(f"Name: {coupon['name']}, Detail: {coupon['detail']}")

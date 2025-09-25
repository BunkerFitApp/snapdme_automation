import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.revenue_page import RevenuePage

def test_revenue_flow(driver):
	driver.get("https://dev.events.snapdme.com/")

	# Login
	login_page = LoginPage(driver)
	login_page.enter_email("your_email@example.com")
	login_page.enter_password("your_password")
	login_page.click_continue()

	# Go to Revenue page via sidebar
	revenue_page = RevenuePage(driver)
	revenue_page.click_revenue_sidebar()

	# Print tile values
	tile_values = revenue_page.get_tile_values()
	print("Revenue Tile Values:")
	for idx, value in enumerate(tile_values, 1):
		print(f"Tile {idx}: {value}")

	# Print revenue list
	revenue_list = revenue_page.get_revenue_list()
	print("Revenue List:")
	for rev in revenue_list:
		print(f"Name: {rev['name']}, Amount: {rev['amount']}")

	# Print total revenue
	total = revenue_page.calculate_total_revenue()
	print(f"Total Revenue: ₹{total}")

	# Print highest revenue entry
	if revenue_list:
		highest = max(revenue_list, key=lambda x: float(x['amount'].replace(',', '').replace('₹', '').strip()))
		print(f"Highest Revenue Entry: Name: {highest['name']}, Amount: {highest['amount']}")

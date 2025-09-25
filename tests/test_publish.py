import pytest
from pages.login_page import LoginPage
from pages.publish_page import PublishPage

def test_publish_event_flow(driver):
	driver.get("https://dev.events.snapdme.com/")

	# Login
	login_page = LoginPage(driver)
	login_page.enter_email("your_email@example.com")
	login_page.enter_password("your_password")
	login_page.click_continue()

	# Go to Publish page via sidebar
	publish_page = PublishPage(driver)
	publish_page.click_publish_sidebar()

	# Publish event
	publish_page.click_publish_event()
	publish_page.confirm_publish()

	# Print success message
	message = publish_page.get_success_message()
	print(f"Publish Success Message: {message}")

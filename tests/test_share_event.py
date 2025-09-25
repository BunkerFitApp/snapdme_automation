import pytest
from pages.login_page import LoginPage
from pages.share_event_page import ShareEventPage

def test_share_event_flow(driver):
	driver.get("https://dev.events.snapdme.com/")

	# Login
	login_page = LoginPage(driver)
	login_page.enter_email("your_email@example.com")
	login_page.enter_password("your_password")
	login_page.click_continue()

	# Go to Share Event page via sidebar
	share_event_page = ShareEventPage(driver)
	share_event_page.click_share_event_sidebar()

	# Copy and print event link
	event_link = share_event_page.copy_event_link()
	print(f"Event Link: {event_link}")

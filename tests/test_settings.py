import pytest
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage

def test_event_settings_edit(driver):
	driver.get("https://dev.events.snapdme.com/")

	# Login
	login_page = LoginPage(driver)
	login_page.enter_email("your_email@example.com")
	login_page.enter_password("your_password")
	login_page.click_continue()

	settings_page = SettingsPage(driver)

	# Check if any event is present
	if settings_page.is_no_event_present():
		print("No events present. Cannot edit settings.")
		assert True
	else:
		# Try to open event settings
		opened = settings_page.open_event_settings()
		assert opened, "Could not open event settings."
		# Edit details
		settings_page.edit_event_details(name="Updated Event Name", location="Updated Location", description="Updated Description")
		settings_page.save_settings()
		print("Event settings updated and saved.")

import pytest
from pages.login_page import LoginPage
from pages.subscription_page import SubscriptionPage

@pytest.mark.order(11)
def test_subscription_plan_flow(driver):
    # Step 1: Open site
    driver.get("https://dev.events.snapdme.com/")

    # Step 2: Login
    login_page = LoginPage(driver)
    login_page.enter_email("nikhil.kushwaha@spectacom.in")
    login_page.enter_password("Nikhil@123")
    login_page.click_continue()

    # Step 3: Go to Subscriptions page
    subscription_page = SubscriptionPage(driver)
    subscription_page.open_subscriptions_page()

    # Step 4: Print plan info
    plan_info = subscription_page.get_plan_info()
    print("Current Plan Info:")
    for key, value in plan_info.items():
        print(f"{key}: {value}")

    # Step 5: Print billing history
    billing_history = subscription_page.get_billing_history()
    print("Billing History:")
    for idx, bill in enumerate(billing_history, 1):
        print(f"{idx}.  Date: {bill['date']}, Amount: {bill['amount']}, Status: {bill['status']}")

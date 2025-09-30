import os
import pytest
import allure
from utils.driver_factory import get_driver
from pytest_html import extras
import subprocess
import sys



@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshots for every test case (pass/fail) and attach to pytest-html & Allure
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")

            try:
                driver.save_screenshot(screenshot_path)
                if os.path.exists(screenshot_path):
                    extra.append(extras.image(screenshot_path))

                    # ✅ Attach to Allure
                    with open(screenshot_path, "rb") as f:
                        allure.attach(
                            f.read(),
                            name=item.name,
                            attachment_type=allure.attachment_type.PNG
                        )
            except Exception as e:
                print(f"⚠️ Screenshot failed: {e}")

        report.extra = extra

def pytest_sessionfinish(session, exitstatus):
    """
    This will run after all tests complete.
    Automatically generates and opens Allure report.
    """
    try:
        # Generate allure report
        subprocess.run([sys.executable, "-m", "allure", "generate", "reports", "-o", "allure-report", "--clean"], check=True)
        # Open allure report in browser
        subprocess.run([sys.executable, "-m", "allure", "open", "allure-report"], check=True)
    except Exception as e:
        print(f"⚠️ Could not open Allure report: {e}")
import os
import pytest
from utils.driver_factory import get_driver
from pytest_html import extras


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshots for every test case (pass/fail) and attach to pytest-html
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
                    # Embed in report
                    extra.append(extras.image(screenshot_path))
            except Exception as e:
                print(f"⚠️ Screenshot failed: {e}")

        report.extra = extra

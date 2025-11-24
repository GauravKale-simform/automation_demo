import os
import shutil

import pytest
from datetime import datetime
from utilities.driver_factory import create_driver

@pytest.fixture(scope="session", autouse=True)
def cleanup_screenshots():
    folder = "screenshots"

    if os.path.exists(folder):
        shutil.rmtree(folder)   # for deleting all older images
    os.makedirs(folder)
    print("\nOld screenshots deleted. Fresh folder created.")

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "test_report", report)

@pytest.fixture(autouse=True)
def screenshot_on_finish(request, driver):
    yield
    report = request.node.test_report
    if report.when == "call":

        test_name = request.node.name
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Capture screenshot
        driver.save_screenshot(file_path)
        print(f"\nScreenshot saved: {file_path}")

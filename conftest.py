import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.binary_location = brave_path
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service("drivers/chromedriver.exe"), options=options)
    driver.get("https://v2.hairnerds.id/")
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        driver = item.funcargs['driver']
        driver.save_screenshot(f"screenshots/failed_test_{item.name}.png")
    elif report.passed:
        driver = item.funcargs['driver']
        driver.save_screenshot(f"screenshots/passed_test_{item.name}.png")
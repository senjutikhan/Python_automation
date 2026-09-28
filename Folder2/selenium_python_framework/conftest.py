import os
import pytest
from utils.driver_factory import get_driver
from utils.config_reader import get_config


@pytest.fixture(scope="function")
def setup(request):
    browser = get_config("basic info", "browser")
    url = get_config("basic info", "url")

    driver = get_driver(browser)
    driver.get(url)
    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to pytest-html report
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra
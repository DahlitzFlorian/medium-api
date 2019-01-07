"""
Alternative Medium API.

An alternative Medium API for interacting with user specific data.
"""

import platform

from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


__version__ = "0.0.1"


def _get_browser():
    os_mapping = {
        "Windows": "windows.exe",
        "Darwin": "macosx",
        "Linux": "linux"
    }

    os_type = platform.system()

    if os_type not in os_mapping:
        raise EnvironmentError("Unsupported system type: {}".format(os_type))

    os_info = os_mapping[os_type]

    try:
        filename = "geckodriver-" + os_info
        executable_path = Path(__file__).resolve().parent / "drivers" / filename
        capabilities = DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False
        test_browser = webdriver.Firefox(capabilities=capabilities, executable_path=str(executable_path))
        test_browser.get("https://google.com")

        return test_browser
    except WebDriverException:
        try:
            filename = "chromedriver-" + os_info
            executable_path = Path(__file__).resolve().parent / "drivers" / filename
            capabilities = DesiredCapabilities().CHROME
            capabilities["marionette"] = False
            test_browser = webdriver.Chrome(capabilities=capabilities, executable_path=str(executable_path))
            test_browser.get("https://google.com")

            return test_browser
        except WebDriverException:
            raise EnvironmentError("No supported browser installed. Install Firefox or Chrome.")


browser = _get_browser()

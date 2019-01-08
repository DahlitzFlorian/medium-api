"""
Alternative Medium API.

An alternative Medium API for interacting with user specific data.
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


__version__ = "0.0.1"


def _get_browser():
    try:
        test_browser = webdriver.Firefox()
        test_browser.get("https://google.com")

        return test_browser
    except WebDriverException:
        try:
            test_browser = webdriver.Chrome()
            test_browser.get("https://google.com")

            return test_browser
        except WebDriverException:
            raise EnvironmentError("No supported browser installed. Install Firefox or Chrome.")


browser = _get_browser()

"""
Alternative Medium API.

An alternative Medium API for interacting with user specific data.
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


__version__ = "0.0.1"


def _get_browser():
    try:
        options = webdriver.firefox.options.Options()
        options.headless = True
        test_browser = webdriver.Firefox(options=options)
        test_browser.get("https://google.com")

        return test_browser
    except WebDriverException:
        try:
            options = webdriver.chrome.options.Options()
            options.headless = True
            test_browser = webdriver.Chrome(options=options)
            test_browser.get("https://google.com")

            return test_browser
        except WebDriverException:
            raise EnvironmentError("No supported browser installed. Install Firefox or Chrome.")


browser = _get_browser()

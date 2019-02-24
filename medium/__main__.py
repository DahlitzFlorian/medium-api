"""Main module used for exploration stuff."""

from loguru import logger

from medium import browser


website_link = (
    "https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F&operation=login"
)
email = ""
password = ""

browser.get(website_link)

try:
    email_button = browser.find_element_by_css_selector("button.js-emailButton")
    email_button.click()
    email_field = browser.find_element_by_name("email")
    email_field.send_keys(email)
    login_button = browser.find_element_by_css_selector(
        "button[data-action-value='login']"
    )
    login_button.click

    logger.debug(browser.page_source)
except Exception as e:
    print(e)

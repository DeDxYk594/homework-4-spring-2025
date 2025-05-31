import time
import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver


class PageNotOpenedExeption(Exception):
    pass

DEFAULT_TIMEOUT = 5


class BasePage(object):
    url: str
    driver: WebDriver
    locators = basic_locators.BasePageLocators
    base_page_locators = basic_locators.BasePageLocators
    compare_url_by_prefix: bool = False

    def is_opened(self, timeout: int | None = None):
        timeout = timeout or DEFAULT_TIMEOUT
        started = time.time()
        while time.time() - started < timeout:
            if self.compare_url_by_prefix and self.driver.current_url.startswith(
                self.url
            ):
                return True

            if self.driver.current_url == self.url:
                return True
            print(self.driver.current_url)
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout: int | None = None):
        timeout = timeout or DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator: Tuple[str, str], timeout: int | None = None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

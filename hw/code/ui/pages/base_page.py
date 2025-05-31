import time
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, final, Optional
from selenium.webdriver.remote.webdriver import WebDriver
import re
from ..utils import Locator


class PageNotOpenedExeption(Exception):
    pass


DEFAULT_TIMEOUT = 5


class BasePage(object):
    url_pattern: re.Pattern[str]  # should not consider 'https://' prefix
    driver: WebDriver
    base_page_locators = basic_locators.BasePageLocators

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.is_opened()

    @final
    def is_opened(self, timeout: Optional[int] = None):
        timeout = timeout or DEFAULT_TIMEOUT
        started = time.time()
        while time.time() - started < timeout:
            url_without_prefix = self.driver.current_url.removeprefix("https://")
            if self.url_pattern.fullmatch(url_without_prefix):
                return True

        raise PageNotOpenedExeption(
            f"{self.url_pattern} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    @final
    def wait(self, timeout: Optional[int] = None):
        timeout = timeout or DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    @final
    def find(
        self, locator: Tuple[str, str], timeout: Optional[int] = None
    ) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @final
    def click(self, locator: Locator, timeout: Optional[int] = None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

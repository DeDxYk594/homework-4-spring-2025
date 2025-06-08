from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, final, Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import re
from ..utils import Locator


class PageNotOpenedException(Exception):
    pass


DEFAULT_TIMEOUT = 8


class BasePage(object):
    url_pattern: re.Pattern[str]  # should not consider 'https://' prefix
    driver: WebDriver
    base_page_locators = basic_locators.BasePageLocators

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait_until_opened()

    @final
    def wait_until_opened(self, timeout: Optional[int] = None):
        """Wait for the page to be opened by checking URL pattern match."""
        timeout = timeout or DEFAULT_TIMEOUT

        def current_url_matches_pattern(driver: WebDriver) -> bool:
            url_without_prefix = driver.current_url.removeprefix("https://")
            return bool(self.url_pattern.fullmatch(url_without_prefix))

        try:
            self.wait(timeout).until(current_url_matches_pattern)
            return True
        except TimeoutException:
            raise PageNotOpenedException(
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

    def find_all(self, locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

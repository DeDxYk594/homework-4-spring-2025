from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from ..locators.group_editing_page_locators import GroupEditingPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re


class GroupEditingPage(BasePage):
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/[0-9]*\/groups/.*")
    locators = GroupEditingPageLocators

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._web_driver_wait = WebDriverWait(driver, 10)

    def change_title(self, new_title: str) -> None:
        self.click(self.locators.EDITABLE_TITLE_EDIT_BUTTON)
        title_input = self._web_driver_wait.until(
            EC.element_to_be_clickable(self.locators.EDITABLE_TITLE_EDIT_BUTTON)
        )
        ActionChains(self.driver).send_keys_to_element(title_input, new_title)\
                                .send_keys(Keys.ENTER)\
                                .perform()

    def save_changes(self) -> None:
        self.click(self.locators.SAVE_BUTTON)

    def get_title(self) -> str:
        title_element: WebElement = self._web_driver_wait.until(
            EC.visibility_of_element_located(self.locators.EDITABLE_TITLE)
        )
        return title_element.text

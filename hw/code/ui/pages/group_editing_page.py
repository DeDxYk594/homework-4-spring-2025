from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from ..locators.group_editing_page_locators import GroupEditingPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time


class GroupEditingPage(BasePage):
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/[0-9]*\/groups/.*")
    locators = GroupEditingPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def change_title(self, new_title: str):
        self.click(self.locators.EDITABLE_TITLE_EDIT_BUTTON)
        time.sleep(1)
        ActionChains(self.driver).send_keys(new_title).send_keys().send_keys(
            Keys.ENTER
        ).perform()

    def save_changes(self):
        self.click(self.locators.SAVE_BUTTON)

    def get_title(self):
        title_element = self.find(self.locators.EDITABLE_TITLE)
        return title_element.text

from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from ..locators.group_editing_page_locators import GroupEditingPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re


class GroupEditingPage(BasePage):
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/[0-9]*\/groups/.*")
    locators = GroupEditingPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def change_title(self, new_title: str):
        self.click(self.locators.EDITABLE_TITLE)
        self.driver.implicitly_wait(1)
        ActionChains(self.driver).send_keys(new_title).send_keys().send_keys(Keys.ENTER)
        self.driver.refresh()

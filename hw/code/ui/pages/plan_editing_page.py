from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from .group_editing_page import GroupEditingPage
from ..locators.plan_editing_page_locators import PlanEditingPageLocators
import re


class PlanEditingPage(BasePage):
    locators = PlanEditingPageLocators
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/.*")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_group_editing(self):
        self.click(self.locators.GROUP_BUTTON)
        next_page = GroupEditingPage(self.driver)
        return next_page

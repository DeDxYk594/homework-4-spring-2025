from .base_page import BasePage
import re
from selenium.webdriver.remote.webdriver import WebDriver
from ..locators.group_creation_page_locators import GroupCreationPageLocators
from ..pages.ad_creation_page import AdCreationPage
from selenium.webdriver.support import expected_conditions as EC


class GroupCreationPage(BasePage):
    url_pattern = re.compile(
        r"ads\.vk\.com\/hq\/new_create\/ad_plan\/new-site_conversions\/ad_group\/new-ad-group-form.*"
    )
    locators = GroupCreationPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def filling_out_form_ad_groups(self):
        self.click(self.locators.COUNTRY_SELECT)

    def wait_for_continue_button_enabled(self):
        return self.wait().until(
            EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)
        )

    def go_to_ad_creation(self):
        self.wait_for_continue_button_enabled()
        self.click(self.locators.CONTINUE_BUTTON)
        return AdCreationPage(self.driver)

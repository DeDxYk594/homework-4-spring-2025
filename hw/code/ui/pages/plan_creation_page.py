import time
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ..locators.plan_creation_page import PlanCreationPageLocator
from ..pages.group_creation_page import GroupCreationPage
import re


class PlanCreationPage(BasePage):
    url_pattern = re.compile(r"ads.vk.com\/hq\/new_create\/ad_plan")
    locators = PlanCreationPageLocator

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def filling_out_form_company_settings(self):
        self.click(self.locators.SITE_SELECT)

        site_url_input = self.find(self.locators.SITE_URL_INPUT)
        site_url_input.clear()
        site_url_input.send_keys("https://kanban-pumpkin.ru/")
        site_url_input.send_keys(Keys.ENTER)

        description_textarea = self.find(self.locators.OFFER_DESCRIPTION_TEXTAREA)
        description_textarea.clear()
        description_textarea.send_keys(
            "Это тестовое описание кампании для автоматизированного тестирования"
        )

        self.click(self.locators.PRICED_GOAL_INPUT)
        first_goal_option = self.find(self.locators.PRICED_GOAL_INPUT)
        first_goal_option.click()

        self.click(self.locators.AUTOBIDDING_MODE_INPUT)
        first_bidding_option = self.find(self.locators.AUTOBIDDING_MODE_INPUT)
        first_bidding_option.click()

        targeting_input = self.find(self.locators.TARGETING_INPUT)
        targeting_input.clear()
        targeting_input.send_keys("100")

        self.click(self.locators.CALENDAR_BUTTON)
        self.click(self.locators.DAY_SELECT)

    def wait_for_continue_button_enabled(self):
        return self._wait.until(
            EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)
        )

    def go_to_group_creation(self):
        self.wait_for_continue_button_enabled()
        self.click(self.locators.CONTINUE_BUTTON)
        return GroupCreationPage(self.driver)

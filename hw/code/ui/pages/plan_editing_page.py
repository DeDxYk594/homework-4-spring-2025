from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .group_editing_page import GroupEditingPage
from ..locators.plan_editing_page_locators import PlanEditingPageLocators
import re
from typing import Optional


class PlanEditingPage(BasePage):
    locators = PlanEditingPageLocators
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/.*")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_opened(self) -> bool:

        return self.wait().until(
            EC.visibility_of_element_located(self.locators.PAGE_TITLE)
        ).is_displayed()

    def get_plan_title(self) -> Optional[str]:
        try:
            return self.wait().until(
                EC.visibility_of_element_located(self.locators.PLAN_TITLE)
            ).text
        except:
            return None

    def change_title(self, new_title: str) -> None:
        title_field = self.wait().until(
            EC.element_to_be_clickable(self.locators.PLAN_TITLE_INPUT)
        )
        title_field.clear()
        title_field.send_keys(new_title)

    def save_changes(self) -> None:
        self.wait().until(
            EC.element_to_be_clickable(self.locators.SAVE_BUTTON)
        ).click()
        self.wait().until(
            EC.invisibility_of_element_located(self.locators.SAVE_LOADER)
        )

    def go_to_group_editing(self) -> GroupEditingPage:
        self.click(self.locators.GROUP_BUTTON)
        next_page = GroupEditingPage(self.driver)
        return next_page

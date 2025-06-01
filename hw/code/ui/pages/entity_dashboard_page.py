from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from .plan_editing_page import PlanEditingPage
from ..locators.entity_dashboard_page_locators import EntityDashboardPageLocator
import re
from selenium.webdriver.common.action_chains import ActionChains


class EntityDashboardPage(BasePage):
    url_pattern = re.compile(r"ads\.vk\.com/hq/dashboard/ad_plans.*")
    locators = EntityDashboardPageLocator

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_plan_editing(self):
        row_elem = self.find(self.locators.PLAN_ROW)
        ActionChains(self.driver).move_to_element(row_elem).perform()
        self.click(self.locators.EDIT_BUTTON)
<<<<<<< HEAD
        
    def go_to_create_plan(self):
        self.click(self.locators.CREATE_BUTTON)
=======
        next_page = PlanEditingPage(self.driver)
        return next_page
>>>>>>> d1b71331e39af997ebe683aa5c6230d9e79da930

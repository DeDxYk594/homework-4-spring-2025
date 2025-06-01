from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from ..locators.entity_dashboard_page_locators import EntityDashboardPageLocator
import re
from selenium.webdriver.common.action_chains import ActionChains


class EntityDashboardPage(BasePage):
    url_pattern = re.compile(r"ads\.vk\.com/hq/dashboard/ad_plans.*")
    locators = EntityDashboardPageLocator

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def go_to_edit_campaign(self):
        row_elem = self.find(self.locators.PLAN_ROW)
        ActionChains(self.driver).move_to_element(row_elem).perform()

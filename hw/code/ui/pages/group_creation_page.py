from .base_page import BasePage
import re
from selenium.webdriver.remote.webdriver import WebDriver
from ..locators.group_creation_page_locators import GroupCreationPageLocators
from ..pages.ad_creation_page import AdCreationPage
from selenium.webdriver.support import expected_conditions as EC


def remove_non_digits(s: str):
    result: list[str] = []
    for char in s:
        if char.isdigit():
            result.append(char)
    return "".join(result)


class GroupCreationPage(BasePage):
    url_pattern = re.compile(
        r"ads\.vk\.com\/hq\/new_create\/ad_plan\/new-site_conversions\/ad_group\/new-ad-group-form.*"
    )
    locators = GroupCreationPageLocators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def fill_with_simple_test_data(self):
        self.click(self.locators.select_city("Москва"))

    def wait_for_continue_button_enabled(self):
        return self.wait().until(
            EC.element_to_be_clickable(self.locators.CONTINUE_BUTTON)
        )

    def go_to_ad_creation(self):
        self.wait_for_continue_button_enabled()
        self.click(self.locators.CONTINUE_BUTTON)
        return AdCreationPage(self.driver)

    def select_city(self, city: str):
        self.click(self.locators.select_city(city))

    def get_predicted_auditory(self):
        pred = self.find(self.locators.PREDICTION_AUDITORY)
        return int(remove_non_digits(pred.text))

    def wait_until_predicted_auditory_changed(self):
        initial_predicted_auditory = self.get_predicted_auditory()

        def predicted_auditory_changed():
            return self.get_predicted_auditory() != initial_predicted_auditory

        self.wait().until(lambda _: predicted_auditory_changed())

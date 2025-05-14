import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By
import json


@pytest.fixture(scope="session")
def credentials():
    pass


@pytest.fixture(scope="session")
def cookies(credentials, config):
    pass


class MainPageLocators:
    registration_button = (By.XPATH, "//a[contains(text(), 'Регистрация')]")


class BaseCase:
    authorize = True


class MainPage(BasePage):
    locators = MainPageLocators
    url = "https://ads.vk.com/"

    def __init__(self, driver):
        driver.get(self.url)
        super().__init__(driver)
        self.is_opened()

    def go_to_registration(self):
        self.find(self.locators.registration_button)
        self.click(self.locators.registration_button)

        return LoginPage(self.driver)


class LoginPage(BasePage):
    compare_url_by_prefix = True
    url = "https://id.vk.com/auth"

    def __init__(self, driver):
        driver.get(self.url)
        super().__init__(driver)
        self.is_opened()

    def login(self, user, password):
        return MainPage(self.driver)


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials, driver):
        page = MainPage(driver)
        page.go_to_registration()
        time.sleep(10)
        assert 2 + 2 == 5

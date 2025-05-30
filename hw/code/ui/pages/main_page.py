from selenium.webdriver.common.by import By
import allure
from ui.locators.main_page_locators import MainPageLocators
from ui.pages.base_page import BasePage
import re


class MainPage(BasePage):
    """Главная страница рекламного кабинета"""
    url_pattern = re.compile("https://ads.vk.com/hq/overview")
    locators = MainPageLocators

    @allure.step("Step 2")
    def go_to_events_page(self):
        events_button = self.find(self.locators.EVENTS)
        # self.click(events_button)
        self.click((By.ID, 'events'))
        return EventsPage(self.driver)

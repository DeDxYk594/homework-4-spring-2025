from .base_page import BasePage
from locators import vk_id as loc


class VkIdPage(BasePage):
    url = "https://id.vk.com/about/id"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        print("HERE")
        button = self.find(loc.START_LOGIN_LOCATOR)
        self.click_unclickable(loc.START_LOGIN_LOCATOR)
        self.wait(10)

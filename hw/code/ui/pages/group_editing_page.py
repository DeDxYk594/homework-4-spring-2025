from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
import re

class GroupEditingPage (BasePage):
    url_pattern = re.compile(r"ads.vk.com\/hq\/dashboard\/plans\/[0-9]*\/groups/.*")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

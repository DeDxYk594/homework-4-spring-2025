from time import sleep
from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.locators.audience_page import AudiencePageLocator
import re
from selenium.webdriver.support import expected_conditions as EC


class AudiencePage(BasePage):
    url_pattern = re.compile(r"ads\.vk\.com/hq/audience")

    def __init__(self, driver):
        super().__init__(driver)

    def click_create_audience(self):
        self.click(AudiencePageLocator.CREATE_AUDIENCE_BUTTON)

    def enter_audience_name(self, name: str):
        name_input = self.find(AudiencePageLocator.AUDIENCE_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)

    def click_add_source(self):
        self.click(AudiencePageLocator.ADD_SOURCE_BUTTON)


    def click_social_group_button(self):
        self.click(AudiencePageLocator.SOCIAL_GROUP_BUTTON)

    def search_group(self, name: str):
        search_input = self.find(AudiencePageLocator.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(name)

    def click_communities_header(self):
        self.click(AudiencePageLocator.VK_COMMUNITIES_HEADER)


    def click_first_group_result(self):
        self.click(AudiencePageLocator.FIRST_GROUP_RESULT)

    def click_exit_group_selection(self):
        self.click(AudiencePageLocator.EXIT_GROUP_SELECTION_TITLE)

    def click_save_button(self):
        buttons = self.driver.find_elements(*AudiencePageLocator.SAVE_BUTTON)
        for btn in buttons:
            if btn.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                sleep(0.5)
                self.driver.execute_script("arguments[0].click();", btn)
                break



        

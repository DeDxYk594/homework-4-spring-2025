from time import sleep
from ..pages.base_page import BasePage
from ..locators.audience_page_locators import AudiencePageLocator
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    # def click_add_source(self):
    #     self.click(AudiencePageLocator.ADD_SOURCE_BUTTON)
    def click_add_source(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(AudiencePageLocator.ADD_SOURCE_BUTTON))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)

    def click_social_group_button(self):
        self.click(AudiencePageLocator.SOCIAL_GROUP_BUTTON)

    def search_group(self, name: str):
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.visibility_of_element_located(AudiencePageLocator.SEARCH_INPUT))

        print("[DEBUG] is_displayed:", search_input.is_displayed())
        print("[DEBUG] is_enabled:", search_input.is_enabled())

        assert search_input.is_displayed(), "Input not visible"
        assert search_input.is_enabled(), "Input not enabled"

        search_input.click()
        search_input.send_keys(name)
        sleep(2)


    def click_communities_header(self):
        self.click(AudiencePageLocator.VK_COMMUNITIES_HEADER)

    def click_first_group_result(self):
        self.click(AudiencePageLocator.FIRST_GROUP_RESULT)

    def select_first_group_item(self):
        item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AudiencePageLocator.FIRST_RESULT_ITEM)
        )
        item.click()


    def click_exit_group_selection(self):
        self.click(AudiencePageLocator.EXIT_GROUP_SELECTION_TITLE)

    def click_save_button(self):
        buttons = self.driver.find_elements(*AudiencePageLocator.SAVE_BUTTON)
        for btn in buttons:
            if btn.is_displayed():
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", btn
                )
                sleep(0.5)
                self.driver.execute_script("arguments[0].click();", btn)
                break
    
    def click_exclude_source(self):
        exclude_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AudiencePageLocator.EXCLUDE_SOURCE_BUTTON)
        )
        exclude_btn.click()

    def click_add_source_from_list(self):
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(AudiencePageLocator.ADD_SOURCE_BUTTON_IN_LIST))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        sleep(0.5)
        self.driver.execute_script("arguments[0].click();", btn)
    

    def click_app_category_button(self):
        self.click(AudiencePageLocator.APP_CATEGORY_BUTTON)

import re
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from ..pages.base_page import BasePage
from ..locators.ad_creation_page_locators import AdCreationPageLocator as Locators


class AdCreationPage(BasePage):
    url_pattern = re.compile(r"ads\.vk\.com/hq/new_create/ad_plan/new-site_conversions.*")
    locators = Locators

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def edit_campaign_title(self, name: str):
        self.click(self.locators.EDIT_ICON)
        title_input = self.find(self.locators.TITLE_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", title_input)
        title_input.clear()
        title_input.send_keys(name)

    def get_ad_title(self):
        title_input = self.find(self.locators.HEADER_INPUT)
        return title_input.text

    def edit_ad_title(self, name: str):
        self.wait().until(EC.visibility_of_element_located(self.locators.HEADER_INPUT))
        title_input = self.find(self.locators.HEADER_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", title_input)
        title_input.send_keys(name)

    def edit_ad_short_description(self, description: str):
        self.wait().until(EC.visibility_of_element_located(self.locators.DESCRIPTION_INPUT))
        desc = self.find(self.locators.DESCRIPTION_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", desc)
        desc.send_keys(description)
        return desc.get_attribute("value") or desc.text

    def get_preview_title(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.PREVIEW_TITLE))
        title = self.driver.find_element(*self.locators.PREVIEW_TITLE)
        return title.text

    def get_title_error_message(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.TITLE_ERROR_MESSAGE))
        error = self.driver.find_element(*self.locators.TITLE_ERROR_MESSAGE)
        return error.text

    def get_description_error_message(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.DESCRIPTION_BLOCK_ERROR))
        error = self.driver.find_element(*self.locators.DESCRIPTION_BLOCK_ERROR)
        return error.text

    def get_preview_video(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.PREVIEW_VIDEO))
        return self.driver.find_element(*self.locators.PREVIEW_VIDEO)

    def get_preview_stream(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.PREVIEW_STREAM))
        return self.driver.find_element(*self.locators.PREVIEW_STREAM)

    def select_site_option(self):
        self.click(self.locators.SITE_OPTION)

    def enter_site_url(self, url: str):
        input_ = self.find(self.locators.SITE_INPUT)
        input_.clear()
        input_.send_keys(url)

    def enter_budget(self, amount: str):
        self.wait().until(EC.presence_of_element_located(self.locators.BUDGET_INPUT))
        budget_input = self.find(self.locators.BUDGET_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", budget_input)
        ActionChains(self.driver).move_to_element(budget_input).perform()
        budget_input.click()
        budget_input.send_keys(Keys.CONTROL, "a")
        budget_input.send_keys(Keys.BACKSPACE)
        budget_input.send_keys(amount)

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_publish(self):
        self.wait().until(EC.element_to_be_clickable(self.locators.PUBLISH_BUTTON))
        self.click(self.locators.PUBLISH_BUTTON)

    def select_moscow_region(self):
        self.click(self.locators.REGION_MOSCOW_BUTTON)

    def generate_title(self, title: str):
        self.click(self.locators.TITLE_GENERATE_ICON)
        self.wait().until(EC.presence_of_element_located(self.locators.GENERATED_TITLE_TEXTAREA))
        textarea = self.find(self.locators.GENERATED_TITLE_TEXTAREA)
        textarea.clear()
        textarea.send_keys(title)
        self.click(self.locators.APPLY_GENERATED_TITLE_BUTTON)

    def click_choose_logo(self):
        self.click(self.locators.CHOOSE_LOGO_BUTTON)

    def open_photo_stock_tab(self):
        self.click(self.locators.PHOTO_STOCK_TAB)

    def choose_generated_logo(self):
        self.click(self.locators.GENERATED_LOGO_ITEM)

    def select_second_media_option(self):
        print("Ожидание появления второго media-option изображения...")
        elements = self.wait().until(
            lambda d: d.find_elements(*self.locators.SECOND_MEDIA_OPTION_LOCATOR)
        )
        if len(elements) >= 2:
            elements[1].click()
        else:
            raise Exception("Второе изображение media-option не найдено")

    def change_photo(self):
        self.wait().until(EC.element_to_be_clickable(self.locators.CHANGE_IMAGES_BUTTON))
        self.click(self.locators.CHANGE_IMAGES_BUTTON)
        self.click(self.locators.IMAGE_SELECT)

    def fill_with_simple_test_data(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.HEADER_INPUT))
        header = self.find(self.locators.HEADER_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", header)
        header.send_keys("Тестовое название")

        self.wait().until(EC.visibility_of_element_located(self.locators.DESCRIPTION_INPUT))
        desc = self.find(self.locators.DESCRIPTION_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", desc)
        desc.send_keys("Тестовое описание")

        self.click(self.locators.LOGO_SELECT)
        self.wait().until(EC.element_to_be_clickable(self.locators.IMAGE_SELECT))
        self.click(self.locators.IMAGE_SELECT)

        self.click(self.locators.MEDIA_BUTTON)
        self.click(self.locators.IMAGE_SELECT)
        self.click(self.locators.ADD_IMAGES_BUTTON)
        self.click(self.locators.SAVE_DRAFTS_BUTTON)

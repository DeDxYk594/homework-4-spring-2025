from ..pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..locators.ad_creation_page_locators import AdCreationPageLocator
import time


class AdCreationPage(BasePage):
    url_pattern = re.compile(r"ads.vk.com/hq/new_create/ad_plan/new-site_conversions.*")
    locators = AdCreationPageLocator

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_ad_title(self):
        title_input = self.find(self.locators.HEADER_INPUT)
        return title_input.text

    def edit_ad_title(self, name: str):
        self.wait().until(EC.visibility_of_element_located(self.locators.HEADER_INPUT))
        title_input = self.find(self.locators.HEADER_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", title_input)
        title_input.send_keys(name)

    def edit_ad_short_description(self, description: str):
        self.wait().until(
            EC.visibility_of_element_located(self.locators.DESCRIPTION_INPUT)
        )
        desc = self.find(self.locators.DESCRIPTION_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", desc)
        desc.send_keys(description)
        actual_text = (
            self.driver.execute_script("return arguments[0].value", desc)
            or desc.get_attribute("value")
            or desc.text
        )
        return actual_text

    def change_photo(self):
        self.wait().until(
            EC.element_to_be_clickable(self.locators.CHANGE_IMAGES_BUTTON)
        )
        self.click(self.locators.CHANGE_IMAGES_BUTTON)
        self.click(self.locators.IMAGE_SELECT)

    def click_button_by_text(self, text):
        locator = (By.XPATH, f"//button[.//span[text()='{text}']]")
        self.wait().until(EC.visibility_of_element_located(locator))
        button = self.driver.find_element(*locator)
        button.click()

    def get_preview_title(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.PREVIEW_TITLE))
        desc = self.driver.find_element(*self.locators.PREVIEW_TITLE)
        actual_text = (
            self.driver.execute_script("return arguments[0].value", desc)
            or desc.get_attribute("value")
            or desc.text
        )
        return actual_text

    def get_title_error_message(self):
        self.wait().until(
            EC.visibility_of_element_located(self.locators.TITLE_ERROR_MESSAGE)
        )
        desc = self.driver.find_element(*self.locators.TITLE_ERROR_MESSAGE)
        actual_text = (
            self.driver.execute_script("return arguments[0].value", desc)
            or desc.get_attribute("value")
            or desc.text
        )
        return actual_text

    def get_description_error_message(self):
        self.wait().until(
            EC.visibility_of_element_located(self.locators.DESCRIPTION_BLOCK_ERROR)
        )
        desc = self.driver.find_element(*self.locators.DESCRIPTION_BLOCK_ERROR)
        actual_text = (
            self.driver.execute_script("return arguments[0].value", desc)
            or desc.get_attribute("value")
            or desc.text
        )
        return actual_text

    def get_preview_video(self):
        self.wait().until(EC.visibility_of_element_located(self.locators.PREVIEW_VIDEO))
        return self.driver.find_element(*self.locators.PREVIEW_VIDEO)

    def get_preview_stream(self):
        self.wait().until(
            EC.visibility_of_element_located(self.locators.PREVIEW_STREAM)
        )
        return self.driver.find_element(*self.locators.PREVIEW_STREAM)

    def select_site_option(self):
        self.click(self.locators.SITE_OPTION)

    def enter_site_url(self, url: str):
        site_input = self.find(self.locators.SITE_INPUT)
        site_input.clear()
        site_input.send_keys(url)

    def enter_budget(self, amount: str):
        self.wait().until(EC.presence_of_element_located(self.locators.BUDGET_INPUT))
        budget_input = self.find(self.locators.BUDGET_INPUT)
        budget_input.clear()
        budget_input.send_keys(amount)

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_publish(self):
        self.wait().until(EC.element_to_be_clickable(self.locators.TO_PUBLISH_BUTTON))
        self.click(self.locators.TO_PUBLISH_BUTTON)

    def select_moscow_region(self):
        self.click(self.locators.REGION_MOSCOW_BUTTON)

    def generate_title(self, title: str):
        self.click(self.locators.TITLE_GENERATE_ICON)
        self.wait().until(
            EC.presence_of_element_located(self.locators.GENERATED_TITLE_TEXTAREA)
        )
        textarea = self.find(self.locators.GENERATED_TITLE_TEXTAREA)
        textarea.clear()
        textarea.send_keys(title)
        self.click(self.locators.APPLY_GENERATED_TITLE_BUTTON)

    def select_second_stock_image(self):
        images = self.find_all(
            (By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc")
        )
        if len(images) >= 2:
            images[1].click()

    def select_second_media_option(self):
        options = self.find_all((By.CSS_SELECTOR, "div[data-name^='content:::image_']"))
        if len(options) >= 2:
            options[1].click()

    def click_choose_logo(self):
        self.click((By.CSS_SELECTOR, "button[data-testid='set-global-image']"))

    def open_photo_stock_tab(self):
        self.click((By.CSS_SELECTOR, "div[data-id='photo_stock_and_generated']"))

    def choose_generated_logo(self):
        self.click((By.CSS_SELECTOR, "div[data-testid='image-media-item-loaded']"))

    def select_second_media_option(self):
        self.wait().until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-name^='content:::image_']")
            )
        )
        options = self.find_all((By.CSS_SELECTOR, "div[data-name^='content:::image_']"))
        if len(options) >= 2:
            options[1].click()
        else:
            raise Exception("Не найдено второе изображение для выбора")

    def select_second_stock_image(self):
        self.wait().until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc")
            )
        )
        images = self.find_all(
            (By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc")
        )
        if len(images) >= 2:
            images[1].click()
        else:
            raise Exception("Второе изображение не найдено в фотостоке")

    def click_publish(self):
        self.click((By.CSS_SELECTOR, "button[data-testid='submit-button']"))

    def fill_with_simple_test_data(self):
        """fills ad with the minimum required data to create ad"""
        self.wait().until(EC.visibility_of_element_located(self.locators.HEADER_INPUT))
        header = self.find(self.locators.HEADER_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", header)
        header.send_keys("Тестовое название")

        self.wait().until(
            EC.visibility_of_element_located(self.locators.DESCRIPTION_INPUT)
        )
        desc = self.find(self.locators.DESCRIPTION_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", desc)
        desc.send_keys("Тестовое описание")

        self.click(self.locators.LOGO_SELECT)

        self.wait().until(EC.element_to_be_clickable(self.locators.IMAGE_SELECT))
        self.click(self.locators.IMAGE_SELECT)

        self.click(self.locators.MEDIA_BUTTON)

        self.click(self.locators.IMAGE_SELECT)

        self.click(self.locators.ADD_IMAGES_BUTTON)

        time.sleep(5)

        self.click(self.locators.SAVE_DRAFTS_BUTTON)

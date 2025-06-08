from ..pages.base_page import BasePage
from ..locators.ad_creation_page import AdCreationPageLocator
from selenium.webdriver.remote.webdriver import WebDriver
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdCreationPage(BasePage):
    url_pattern = re.compile(r"ads\.vk\.com/hq/new_create/ad_plan")

    def __init__(self, driver:WebDriver):
        super().__init__(driver)

    def edit_campaign_title(self, name: str):
        self.click(AdCreationPageLocator.TITLE_EDIT_ICON)
        title_input = self.find(AdCreationPageLocator.TITLE_INPUT)
        self.driver.execute_script("arguments[0].innerText = '';", title_input)
        title_input.clear()
        title_input.send_keys(name)

    def select_site_option(self):
        self.click(AdCreationPageLocator.SITE_OPTION)

    def enter_site_url(self, url: str):
        site_input = self.find(AdCreationPageLocator.SITE_INPUT)
        site_input.clear()
        site_input.send_keys(url)

    def enter_budget(self, amount: str):
        self.wait().until(EC.presence_of_element_located(AdCreationPageLocator.BUDGET_INPUT))
        budget_input = self.find(AdCreationPageLocator.BUDGET_INPUT)
        budget_input.clear()
        budget_input.send_keys(amount)


    def click_continue(self):
        self.click(AdCreationPageLocator.CONTINUE_BUTTON)

    def select_moscow_region(self):
        self.click(AdCreationPageLocator.REGION_MOSCOW_BUTTON)

    def generate_title(self, title: str):
        self.click(AdCreationPageLocator.TITLE_GENERATE_ICON)
        self.wait().until(EC.presence_of_element_located(AdCreationPageLocator.GENERATED_TITLE_TEXTAREA))
        textarea = self.find(AdCreationPageLocator.GENERATED_TITLE_TEXTAREA)
        textarea.clear()
        textarea.send_keys(title)
        self.click(AdCreationPageLocator.APPLY_GENERATED_TITLE_BUTTON)

    def select_second_stock_image(self):
        images = self.find_all((By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc"))
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
        self.wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-name^='content:::image_']")))
        options = self.find_all((By.CSS_SELECTOR, "div[data-name^='content:::image_']"))
        if len(options) >= 2:
            options[1].click()
        else:
            raise Exception("Не найдено второе изображение для выбора")

    def select_second_stock_image(self):
        self.wait().until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc")
        ))
        images = self.find_all((By.CLASS_NAME, "PhotoStockImagesPreview_itemContent__DoHxc"))
        if len(images) >= 2:
            images[1].click()
        else:
            raise Exception("Второе изображение не найдено в фотостоке")


    def click_publish(self):
        self.click((By.CSS_SELECTOR, "button[data-testid='submit-button']"))

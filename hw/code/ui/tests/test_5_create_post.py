import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators.ad_creation_page_locators import AdCreationPageLocator
from ..pages.ad_creation_page import AdCreationPage
from ..constants import TEST_SITE_URL, TEST_BUDGET, TEST_GENERATED_TITLE, IMAGE_GENERATION_TIMEOUT


def test_create_campaign_with_site(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/new_create/ad_plan")

    wait = WebDriverWait(driver, IMAGE_GENERATION_TIMEOUT)

    # Выбор типа рекламы — "Сайт"
    site_option = wait.until(EC.element_to_be_clickable(AdCreationPageLocator.SITE_OPTION))
    site_option.click()

    # Ввод сайта
    site_input = wait.until(EC.visibility_of_element_located(AdCreationPageLocator.SITE_INPUT))
    site_input.send_keys(TEST_SITE_URL)
    site_input.send_keys(Keys.TAB)

    continue_btn = wait.until(EC.element_to_be_clickable(AdCreationPageLocator.CONTINUE_BUTTON))
    assert continue_btn.is_enabled(), "Кнопка 'Продолжить' неактивна после ввода сайта"
    continue_btn.click()

    # Ввод бюджета
    budget_input = wait.until(EC.visibility_of_element_located(AdCreationPageLocator.BUDGET_INPUT))
    driver.execute_script("arguments[0].scrollIntoView(true);", budget_input)
    budget_input.click()
    budget_input.clear()
    budget_input.send_keys(TEST_BUDGET)
    budget_input.send_keys(Keys.TAB)

    continue_btn = wait.until(EC.element_to_be_clickable(AdCreationPageLocator.CONTINUE_BUTTON))
    assert continue_btn.is_enabled(), "Кнопка 'Продолжить' неактивна после ввода бюджета"
    continue_btn.click()

    # Выбор региона
    moscow_btn = wait.until(EC.element_to_be_clickable(AdCreationPageLocator.REGION_MOSCOW_BUTTON))
    moscow_btn.click()

    continue_btn = wait.until(EC.element_to_be_clickable(AdCreationPageLocator.CONTINUE_BUTTON))
    continue_btn.click()

    # Работа с генерацией объявления
    page = AdCreationPage(driver)

    page.generate_title(TEST_GENERATED_TITLE)
    page.click_choose_logo()
    page.open_photo_stock_tab()
    page.choose_generated_logo()

    # Ждём, пока появится хотя бы 2 изображения
    wait.until(lambda d: len(d.find_elements(*AdCreationPageLocator.IMAGE_ITEM)) > 1)

 
    page.select_second_media_option()

    page.click_publish()

import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.ad_creation_page import AdCreationPage


@pytest.mark.ui
def test_create_campaign_with_site(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/new_create/ad_plan")
    page = AdCreationPage(driver)

    @pytest.mark.ui
    def test_create_campaign_with_site(driver: WebDriver):
        driver.get("https://ads.vk.com/hq/new_create/ad_plan")
        page = AdCreationPage(driver)
        page.edit_campaign_title("Новая кампания")
        page.select_site_option()

    # Выбираем тип рекламы "Сайт"
    page.select_site_option()

    page.enter_site_url("kanban-pumpkin.ru")
    page.click_continue()
    page.enter_budget("100")
    page.click_continue()

    # Выбор региона — Москва
    page.select_moscow_region()
    page.click_continue()

    # Генерация заголовка
    page.generate_title("Моя новая публикация")

    page.click_choose_logo()
    page.open_photo_stock_tab()
    page.choose_generated_logo()
    time.sleep(20)
    page.select_second_stock_image()
    # time.sleep(20)
    page.select_second_media_option()
    page.click_publish()
    # time.sleep(20)

import time
import pytest
from hw.code.ui.pages.ad_creation_page import AdCreationPage

def test_create_campaign_with_site(driver):
    driver.get("https://ads.vk.com/hq/new_create/ad_plan")
    page = AdCreationPage(driver)

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

    page.select_second_media_option()
    page.click_publish()

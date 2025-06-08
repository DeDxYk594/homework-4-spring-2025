from time import sleep
import pytest
from hw.code.ui.pages.audience_page import AudiencePage


@pytest.mark.ui
def test_create_audience_with_social_group(driver):
    driver.get("https://ads.vk.com/hq/audience")  
    page = AudiencePage(driver)
    page.click_create_audience()

    page.enter_audience_name("Новая аудитория РИА")
    page.click_add_source()

    page.click_social_group_button()
    page.search_group("РИА новости")
    sleep(2)
    page.click_communities_header()
    sleep(1)
    page.click_first_group_result()
    page.click_exit_group_selection()
    sleep(1)
    print("Нажимаем Сохранить")
    page.click_save_button()

    page.click_save_button()  # сохранение на втором экране

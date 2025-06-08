# TODO: @Achpochmak


from time import sleep
import pytest
from hw.code.ui.pages.audience_page import AudiencePage


@pytest.mark.ui
def test_create_audience_with_social_group(driver):
    driver.get("https://ads.vk.com/hq/audience")  
    page = AudiencePage(driver)
    page.click_create_audience()



    # # Ожидаем появления модалки (если нужно)
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(AudiencePageLocator.AUDIENCE_NAME_INPUT)
    # )

    page.enter_audience_name("Новая аудитория РИА")
    page.click_add_source()

    page.click_social_group_button()
    page.search_group("РИА новости")
    sleep(2)
    page.click_communities_header()
    sleep(1)
    page.click_first_group_result()# тут будет клик по нужному сообществу, если оно отобразится

    # page.click_communities_header()
    # page.click_first_group_result()



    # page.select_first_group()
    page.click_save_button()
    page.click_save_button()  # сохранение на втором экране

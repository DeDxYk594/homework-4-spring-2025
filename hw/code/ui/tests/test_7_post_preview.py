import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage


@pytest.fixture
def setup_ad_creation(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    dashboard_page = EntityDashboardPage(driver)

    plan_creation_page = dashboard_page.go_to_create_plan()
    plan_creation_page.fill_with_simple_test_data()

    group_creation_page = plan_creation_page.go_to_group_creation()
    group_creation_page.fill_with_simple_test_data()

    ad_creation_page = group_creation_page.go_to_ad_creation()
    ad_creation_page.fill_with_simple_test_data()

    return ad_creation_page


@allure.story("Preview Tests")
class TestPreview:
    @allure.step("In column preview")
    def test_preview_in_column(self, setup_ad_creation):
        setup_ad_creation.click_button_by_text("В колонке")
        actual_title = setup_ad_creation.get_preview_title()
        assert actual_title == "Тестовое название"

    @allure.step("Post preview")
    def test_preview_post(self, setup_ad_creation):
        setup_ad_creation.click_button_by_text("Пост")
        actual_title = setup_ad_creation.get_preview_title()
        assert actual_title == "Тестовое название"

    @allure.step("Native block preview")
    def test_preview_native_block(self, setup_ad_creation):
        setup_ad_creation.click_button_by_text("Нативный блок")
        actual_title = setup_ad_creation.get_native_block_preview_title()
        assert actual_title == "Тестовое название"

    @allure.step("Video preview")
    def test_preview_video(self, setup_ad_creation):
        setup_ad_creation.click_button_by_text("Ролик в видео")
        vid = setup_ad_creation.get_preview_video()
        assert vid != None

    @allure.step("Full screen block preview")
    def test_preview_full_screen(self, setup_ad_creation):
        setup_ad_creation.click_button_by_text("Полноэкранный блок")
        vid = setup_ad_creation.get_preview_video()
        assert vid != None

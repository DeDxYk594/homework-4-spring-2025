import pytest
import allure
import time
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
    @pytest.mark.parametrize("button", ["В колонке", "Пост", "Нативный блок"])
    def test_preview_post(self, setup_ad_creation, button):
        setup_ad_creation.click_button_by_text(button)
        actual_title = setup_ad_creation.get_preview_title()
        assert actual_title == "Тестовое название"

    @pytest.mark.parametrize("button_text", ["Полноэкранный блок"])
    @allure.step("Video preview")
    def test_preview_video(self, setup_ad_creation, button_text):
        setup_ad_creation.click_button_by_text(button_text)
        vid = setup_ad_creation.get_preview_video()
        assert vid != None

    @pytest.mark.parametrize("button_text", ["Ролик в видео"])
    @allure.step("Stream preview")
    def test_preview_stream(self, setup_ad_creation, button_text):
        setup_ad_creation.click_button_by_text(button_text)
        stream = setup_ad_creation.get_preview_stream()
        assert stream != None

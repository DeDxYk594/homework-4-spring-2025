import pytest
import allure
import time
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
from ..pages.ad_creation_page import AdCreationPage

ALERT_MESSAGE_TEXT_TOO_LONG = "Сократите текст"


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


@allure.story("Edit post tests")
class TestEditPosts:
    @pytest.mark.parametrize(
        "title,description",
        [
            ("test_title", "test_description"),
        ],
    )
    def test_edit_post_ok(self, setup_ad_creation: AdCreationPage, title, description):
        ad_creation_page = setup_ad_creation

        ad_creation_page.edit_ad_title(title)
        actual_title = ad_creation_page.get_ad_title()
        assert actual_title == title

        actual_text = ad_creation_page.edit_ad_short_description(
            description=description
        )
        assert actual_text == description

        ad_creation_page.change_photo()

    @pytest.mark.parametrize(
        "title",
        [
            ("long_title" * 10),
        ],
    )
    def test_edit_post_long_title_fail(self, setup_ad_creation: AdCreationPage, title):
        ad_creation_page = setup_ad_creation
        ad_creation_page.edit_ad_title(title)
        ad_creation_page.click_publish()
        error_message = ad_creation_page.get_title_error_message()

        assert error_message == ALERT_MESSAGE_TEXT_TOO_LONG

    @pytest.mark.parametrize(
        "description",
        [
            ("long_description" * 10),
        ],
    )
    def test_edit_post_long_description_fail(
        self, setup_ad_creation: AdCreationPage, description
    ):
        ad_creation_page = setup_ad_creation
        ad_creation_page.edit_ad_short_description(description)
        ad_creation_page.click_publish()
        error_message = ad_creation_page.get_description_error_message()

        assert error_message == ALERT_MESSAGE_TEXT_TOO_LONG

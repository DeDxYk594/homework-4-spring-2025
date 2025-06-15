import pytest
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


def test_6_edit_post(driver: WebDriver, setup_ad_creation):
    ad_creation_page = setup_ad_creation

    test_title = "test_title"
    actual_title = ad_creation_page.edit_ad_title(name=test_title)
    assert actual_title == test_title

    test_description = "test_description"
    actual_text = ad_creation_page.edit_ad_short_description(
        description=test_description
    )
    assert actual_text == test_description

    ad_creation_page.change_photo()

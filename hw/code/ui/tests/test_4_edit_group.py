from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
from ..pages.group_editing_page import GroupEditingPage
import pytest


@pytest.fixture
def group_editing_page(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    page = EntityDashboardPage(driver)
    plan_creation_page = page.go_to_create_plan()
    plan_creation_page.fill_with_simple_test_data()
    group_creation_page = plan_creation_page.go_to_group_creation()
    group_creation_page.fill_with_simple_test_data()
    ad_creation_page = group_creation_page.go_to_ad_creation()
    ad_creation_page.fill_with_simple_test_data()
    ad_creation_page.click_publish()

    plan_editing_page = page.go_to_plan_editing()
    group_editing_page = plan_editing_page.go_to_group_editing()
    return group_editing_page


def test_should_save_title_changes_when_changes_saved(
    driver: WebDriver, group_editing_page: GroupEditingPage
):
    old_title = group_editing_page.get_title()
    new_title = "test345" if old_title == "test123" else "test123"
    group_editing_page.change_title(new_title)
    group_editing_page.save_changes()
    driver.refresh()
    assert group_editing_page.get_title() == new_title


def test_should_not_save_title_changes_when_changes_not_saved(
    driver: WebDriver, group_editing_page: GroupEditingPage
):
    old_title = group_editing_page.get_title()
    new_title = "test345" if old_title == "test123" else "test123"
    group_editing_page.change_title(new_title)
    driver.refresh()
    assert group_editing_page.get_title() != new_title

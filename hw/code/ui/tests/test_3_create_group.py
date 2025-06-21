import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
from ..pages.group_creation_page import GroupCreationPage


@pytest.fixture
def group_creation_page(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    dashboard_page = EntityDashboardPage(driver)

    plan_creation_page = dashboard_page.go_to_create_plan()
    url = "https://kanban-pumpkin.ru/"
    main_decription = "Это тестовое описание кампании для автоматизированного тестирования"
    price = "100"
    plan_creation_page.fill_with_simple_test_data(url, main_decription, price)

    return plan_creation_page.go_to_group_creation()


def test_should_change_predicted_auditory_when_region_filter_selected(
    driver: WebDriver, group_creation_page: GroupCreationPage
):
    # given
    initial_predicted_auditory = group_creation_page.get_predicted_auditory()

    # when
    group_creation_page.select_city("Москва")
    group_creation_page.wait_until_predicted_auditory_changed()

    # then
    assert group_creation_page.get_predicted_auditory() != initial_predicted_auditory

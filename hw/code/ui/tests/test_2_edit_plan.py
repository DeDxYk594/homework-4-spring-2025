import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
from ..pages.plan_editing_page import PlanEditingPage


@pytest.fixture
def plan_editing_page(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    dashboard_page = EntityDashboardPage(driver)
    return dashboard_page.go_to_plan_editing()


def test_should_open_plan_editing_page(driver: WebDriver, plan_editing_page: PlanEditingPage):
    """Проверка, что страница редактирования плана открывается корректно"""
    assert "ads.vk.com/hq/dashboard/plans" in driver.current_url
    assert plan_editing_page.is_opened()


def test_should_contain_plan_data(plan_editing_page: PlanEditingPage):
    """Проверка, что страница редактирования содержит данные плана"""
    assert plan_editing_page.get_plan_title() != ""


def test_should_save_changes(plan_editing_page: PlanEditingPage):
    """Проверка сохранения изменений в плане"""
    original_title = plan_editing_page.get_plan_title()
    
    new_title = f"{original_title} [TEST]"
    
    plan_editing_page.change_title(new_title)
    plan_editing_page.save_changes()
    
    assert plan_editing_page.get_plan_title() == new_title
    
    plan_editing_page.change_title(original_title)
    plan_editing_page.save_changes()

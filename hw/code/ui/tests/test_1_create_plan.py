from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage

def test_create_plan(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    dashboard_page = EntityDashboardPage(driver)

    plan_creation_page = dashboard_page.go_to_create_plan()
    plan_creation_page.filling_out_form_company_settings()

    group_creation_page = plan_creation_page.go_to_group_creation()
    group_creation_page.filling_out_form_ad_groups()

    ad_creation_page = group_creation_page.go_to_ad_creation()
    ad_creation_page.fill_with_simple_test_data()

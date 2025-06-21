from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage


def test_create_plan(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    dashboard_page = EntityDashboardPage(driver)

    plan_creation_page = dashboard_page.go_to_create_plan()
    url = "https://kanban-pumpkin.ru/"
    main_decription = "Это тестовое описание кампании для автоматизированного тестирования"
    price = "100"
    plan_creation_page.fill_with_simple_test_data(url, main_decription, price)

    group_creation_page = plan_creation_page.go_to_group_creation()
    group_creation_page.fill_with_simple_test_data()

    ad_creation_page = group_creation_page.go_to_ad_creation()
    title = "Тестовое название"
    description = "Тестовое описание"
    ad_creation_page.fill_with_simple_test_data(title, description)

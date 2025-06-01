# TODO: @zhugeo
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
import time


def test_create_group(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    page = EntityDashboardPage(driver)
    page.is_opened()
    plan_editing_page = page.go_to_plan_editing()
    group_editing_page = plan_editing_page.go_to_group_editing()
    group_editing_page.change_title("Кто прочитал тот пидор")
    time.sleep(10)

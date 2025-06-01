from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
import time

def test_create_plane(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    page = EntityDashboardPage(driver)
    page.is_opened()
    plan_creation_page = page.go_to_create_plan()
    plan_creation_page.filling_out_form()
    time.sleep(10)

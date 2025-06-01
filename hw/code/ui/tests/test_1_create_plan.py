from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
import time

def test_create_plane(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    page = EntityDashboardPage(driver)
    page.is_opened()
    page.go_to_create_plan()
    time.sleep(10)

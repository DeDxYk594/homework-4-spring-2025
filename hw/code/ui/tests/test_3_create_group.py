# TODO: @zhugeo
from selenium.webdriver.remote.webdriver import WebDriver
from ..pages.entity_dashboard_page import EntityDashboardPage
import time
import random


def random_test_number():
    return random.randint(0, 9999)


def test_create_group(driver: WebDriver):
    driver.get("https://ads.vk.com/hq/dashboard/ad_plans")
    page = EntityDashboardPage(driver)
    page.is_opened()
    plan_editing_page = page.go_to_plan_editing()
    group_editing_page = plan_editing_page.go_to_group_editing()
    new_title = f"Новое название {random_test_number()}"
    group_editing_page.change_title(new_title)
    group_editing_page.save_changes()
    driver.refresh()
    assert group_editing_page.get_title() == new_title
    time.sleep(10)

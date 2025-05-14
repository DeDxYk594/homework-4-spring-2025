import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
import json
import time


@pytest.fixture()
def driver(config):
    browser = config["browser"]
    selenoid = config["selenoid"]
    vnc = config["vnc"]
    options = Options()
    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "version": "118.0",
        }
        if vnc:
            capabilities["enableVNC"] = True
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub",
            options=options,
            desired_capabilities=capabilities,
        )
    elif browser == "chrome":
        options.add_argument("--user-data-dir=vkads_userdata")
        options.add_argument("profile-directory=vkads-profile")
        driver = webdriver.Chrome(options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.maximize_window()
    driver.get("https://ads.vk.com")
    assert 2 + 2 == 228
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def all_drivers(config, request):
    url = config["url"]
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)
